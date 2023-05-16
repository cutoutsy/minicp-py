#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/27

'''
import pytest
from minicp.engine.core.minicp import MiniCP
from minicp.search.dfsearch import DFSearch
from minicp.search.search_statistics import SearchStatistics
from minicp.state.copier import Copier
from minicp.cp.factory import *
from minicp.cp.branch_schema import *

class TestIsLessOrEqual:

    def test1(self):
        cp = MiniCP(Copier())
        
        x = makeIntVar(cp, -4, 7) 

        b = makeBoolVar(cp)

        cp.post(IsLessOrEqual(b, x, 3))

        search = makeDfs(cp, firstFail([x]))

        def f():
            assert ((x.min() <= 3 and b.isTrue()) or (x.min() > 3 and b.isFalse())) 

        search.onSolution(f)

        stats = search.solve()

        assert 12 == stats.nSolutions
    
    def test2(self):
        cp = makeSolver()
        x = makeIntVar(cp, -4, 7)

        b = makeBoolVar(cp)

        cp.post(IsLessOrEqual(b, x, -2))

        cp.getStateManager().saveState() 
        cp.post(equal(b, 1))
        assert -2 == x.max()
        cp.getStateManager().restoreState()

        cp.getStateManager().saveState()
        cp.post(equal(b, 0))
        assert -1 == x.min()
        cp.getStateManager().restoreState()
    
    def test3(self):
        cp = makeSolver()
        
        x1 = makeIntVar(cp, -4, 7)
        cp.post(equal(x1, -2))
        b1 = makeBoolVar(cp)
        cp.post(IsLessOrEqual(b1, x1, -2))
        assert b1.isTrue()
        
        x2 = makeIntVar(cp, -4, 7)
        cp.post(equal(x2, -2))
        b2 = makeBoolVar(cp)
        cp.post(IsLessOrEqual(b2, x2, -3))
        assert b2.isFalse()
    
    def test4(self):
        cp = makeSolver()
        x = makeIntVar(cp, -4, 7)
        b = makeBoolVar(cp)

        cp.getStateManager().saveState()
        cp.post(equal(b, 1)) 
        cp.post(IsLessOrEqual(b, x, -2)) 
        assert -2 == x.max()
        cp.getStateManager().restoreState()

        cp.getStateManager().saveState() 
        cp.post(equal(b, 0)) 
        cp.post(IsLessOrEqual(b, x, -2)) 
        assert -1 == x.min()
        cp.getStateManager().restoreState()
    
    def test5(self):
        cp = makeSolver()
        x = makeIntVar(cp, -5, 10)
        b = makeBoolVar(cp)

        cp.getStateManager().saveState()
        cp.post(IsLessOrEqual(b, x, -6))
        assert b.isFixed()
        assert b.isFalse()
        cp.getStateManager().restoreState()

        cp.getStateManager().saveState()
        cp.post(IsLessOrEqual(b, x, 11))
        assert b.isFixed()
        assert b.isTrue()
        cp.getStateManager().restoreState()
    
    def test6(self):
        cp = makeSolver()
        x = makeIntVar(cp, -5, -3)
        b = makeBoolVar(cp)

        cp.getStateManager().saveState()
        cp.post(IsLessOrEqual(b, x, -3))
        assert b.isTrue()
        cp.getStateManager().restoreState()

        