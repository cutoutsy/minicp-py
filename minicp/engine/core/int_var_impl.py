#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/18

'''
from minicp.engine.core.int_var import IntVar
from minicp.engine.core.sparse_set_domain import SparseSetDomain
from minicp.exception.in_consistency_error import InconsistencyError
from minicp.state.state_stack import StateStack
from minicp.engine.core.constraint_closure import ConstraintClosure

class DomainListener:
    def __init__(self, int_val_impl):
        self.int_var_impl = int_val_impl
    
    def empty(self):
        raise InconsistencyError("InconsistencyError")
    
    def fix(self):
        self.int_var_impl.scheduleAll(self.int_var_impl.onFix)
    
    def change(self):
        self.int_var_impl.scheduleAll(self.int_var_impl.onDomin)
    
    def changeMin(self):
        self.int_var_impl.scheduleAll(self.int_var_impl.onBound)
    
    def changeMax(self):
        self.int_var_impl.scheduleAll(self.int_var_impl.onBound)

class IntVarImpl(IntVar):
    def __init__(self, cp, min, max):
        super().__init__()
        self.cp = cp
        self.domain = SparseSetDomain(cp.getStateManager(), min, max)
        self.onDomin = StateStack(cp.getStateManager())
        self.onFix = StateStack(cp.getStateManager())
        self.onBound = StateStack(cp.getStateManager())
    
    def getSolver(self):
        return self.cp

    def isFixed(self):
        return self.domain.isSingleton()
    
    def whenFixed(self, f):
        self.onFix.push(self.constraintClosure(f))
    
    def whenBoundChange(self, f):
       self.onBound.push(self.constraintClosure(f))
    
    def whenDomainChange(self, f):
        self.onDomin.push(self.constraintClosure(f))
    
    def constraintClosure(self, f):
        c = ConstraintClosure(self.cp, f)
        self.getSolver().post(c, False)
        return c

    def min(self):
        return self.domain.min()
    
    def max(self):
        return self.domain.max()
    
    def size(self):
        return self.domain.size()
    
    def scheduleAll(self, constraints):
        # print("scheduleAll run, constraints size = ", len(constraints))
        for i in range(len(constraints)):
            self.cp.schedule(constraints.get(i))

    def remove(self, v):
        self.domain.remove(v, DomainListener(self))
    
    def contains(self, v):
        return self.domain.contains(v)
    
    def fix(self, v):
        self.domain.removeAllBut(v, DomainListener(self))
    
    def removeBelow(self, v):
        self.domain.removeBelow(v, DomainListener(self))

    def removeAbove(self, v):
        self.domain.removeAbove(v, DomainListener(self))

        
    
    def fillArray(self, dest):
        return self.domain.fillArray(dest)
    
    def propagateOnBoundChange(self, c):
        self.onBound.push(c)
    
    def propagateOnFix(self, c):
        self.onFix.push(c)

    def propagateOnDomainChange(self, c):
        self.onDomin.push(c)
    
    
    def __str__(self):
        return str(self.domain)