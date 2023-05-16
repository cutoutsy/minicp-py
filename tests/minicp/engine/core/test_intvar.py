#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/05/04

'''
from minicp.cp.factory import *
from minicp.exception import InconsistencyError
from minicp.engine.core.constraint import Constraint

class MyConstrain(Constraint):
    def __init__(self, x: IntVarImpl, y: IntVarImpl, propagateCalled):
        super().__init__(x.getSolver())
        self.x = x
        self.y = y
        self.propagateCalled = propagateCalled

    def whenFixedCall(self):
        self.propagateCalled = True

    def whenDomainChangeCall(self):
        self.propagateCalled = True

    def post(self):
        self.x.whenFixed(self.whenFixedCall)
        self.y.whenDomainChange(self.whenDomainChangeCall)

class RemoveConstrain(Constraint):
    def __init__(self, x: IntVarImpl, propagateCalled):
        super().__init__(x.getSolver())
        self.x = x
        self.propagateCalled = propagateCalled

    def post(self):
        self.x.propagateOnBoundChange(self)
    
    def propagate(self):
        self.propagateCalled = True


class TestIntVar:

    propagateCalled = False
    
    def testIntVar(self):
        cp = makeSolver()
        x = makeIntVar(cp, 0, 9)
        y = makeIntVar(cp, 0, 9)

        cp.getStateManager().saveState()

        assert False == x.isFixed()
        x.remove(5)
        assert 9 == x.size()
        x.fix(7)
        assert 1 == x.size()
        assert x.isFixed()
        assert 7 == x.min()
        assert 7 == x.max()

        try:
            x.fix(8)
        except InconsistencyError as e:
            print("should have failed")
        
        cp.getStateManager().restoreState()
        cp.getStateManager().saveState()

        assert False == x.isFixed()
        assert 10 == x.size()

        for i in range(10):
            assert True == x.contains(i)
        assert False == x.contains(-1)
    

    def testOnDomainChangeOnBind(self):
        propagateCalled = False

        cp = makeSolver()
        x = makeIntVar(cp, 0, 9)
        y = makeIntVar(cp, 0, 9)

        cons = MyConstrain(x, y, propagateCalled)

        cp.post(cons)
        x.remove(8)
        cp.fixPoint()
        assert False == cons.propagateCalled
        x.fix(4)
        cp.fixPoint()
        assert True == cons.propagateCalled
        cons.propagateCalled = False
        y.remove(10)
        cp.fixPoint()
        assert False == cons.propagateCalled
        y.remove(9)
        cp.fixPoint()
        assert True == cons.propagateCalled
    

    def testArbitraryRangeDomains(self):
        cp = makeSolver()
        x = makeIntVar(cp, -10, 10)

        cp.getStateManager().saveState()

        assert False == x.isFixed()
        x.remove(-9)
        x.remove(-10)


        assert 19 == x.size()
        x.fix(-4)
        assert 1 == x.size()
        assert True == x.isFixed()
        assert -4 == x.min()

        cp.getStateManager().restoreState()

        assert 21 == x.size()

        for i in range(-10, 10 + 1):
            assert True == x.contains(i)
        assert False == x.contains(-11)
    
    
    def testOnBoundChange(self):
        propagateCalled = False

        cp = makeSolver()
        x = makeIntVar(cp, 0, 9)
        y = makeIntVar(cp, 0, 9)
    
        cons = MyConstrain(x, y, propagateCalled)

        cp.post(cons)
        x.remove(8)
        cp.fixPoint()
        assert False == cons.propagateCalled
        x.remove(9)
        cp.fixPoint()
        assert False == cons.propagateCalled
        x.fix(4)
        cp.fixPoint()
        assert True == cons.propagateCalled
        cons.propagateCalled = False
        assert False == y.contains(10)
        y.remove(10)
        cp.fixPoint()
        assert False == cons.propagateCalled
        cons.propagateCalled = False
        y.remove(2)
        cp.fixPoint()
        assert True == cons.propagateCalled
    

    def testRemoveAbove(self):
        propagateCalled = False

        cp = makeSolver()
        x = makeIntVar(cp, 0, 9)

        cons = RemoveConstrain(x, propagateCalled)

        cp.post(cons)
        x.remove(8)
        cp.fixPoint()
        assert False == cons.propagateCalled
        x.removeAbove(8)
        assert 7 == x.max()
        cp.fixPoint()
        assert True == cons.propagateCalled
    

    def testRemoveBelow(self):
        propagateCalled = False
        cp = makeSolver()
        x = makeIntVar(cp, 0, 9)

        cons = RemoveConstrain(x, propagateCalled)

        cp.post(cons)
        x.remove(3)
        cp.fixPoint()
        assert False == cons.propagateCalled
        x.removeBelow(3)
        assert 4 == x.min()
        cp.fixPoint()
        assert True == cons.propagateCalled
        cons.propagateCalled = False

        x.removeBelow(5)
        assert 5 == x.min()
        cp.fixPoint()
        assert True == cons.propagateCalled
        cons.propagateCalled = False
    

    def testFillArray(self):
        cp = makeSolver()
        x = makeIntVar(cp, 2, 9)
        
        x.remove(3)
        x.remove(5)
        x.remove(2)
        x.remove(9)

        values = [0] * 10
        s = x.fillArray(values)
        dom = set()
        for i in range(s):
            dom.add(values[i])
        assert dom == set([4, 6, 7, 8])