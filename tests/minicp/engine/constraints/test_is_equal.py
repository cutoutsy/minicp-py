#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/25

'''
from minicp.engine.core.minicp import MiniCP
from minicp.engine.core.int_var_impl import IntVarImpl
from minicp.engine.constraints.not_equal import NotEqual
from minicp.engine.constraints.less_or_equal import LessOrEqual
from minicp.search.dfsearch import DFSearch
from minicp.search.search_statistics import SearchStatistics
from minicp.state.copier import Copier
from minicp.engine.constraints.not_equal_num import NotEqualNum
from minicp.engine.constraints.equal_num import EqualNum
from minicp.engine.constraints.sum import Sum
from minicp.engine.core.int_var_view_mul import IntVarViewMul
from minicp.engine.core.bool_var_impl import BoolVarImpl
from minicp.engine.constraints.is_equal import IsEqual
from minicp.cp.factory import *
from minicp.cp.branch_schema import *

class TestIsEqual:

    def test1(self):
        cp = makeSolver()

        x = makeIntVar(cp, -4, 7)

        b = isEqual(x, -2)

        search = makeDfs(cp, firstFail([x]))

        def onSolution():
            if x.min() == -2:
                assert b.isTrue()
        
        search.onSolution(onSolution)
        stats = search.solve()

        assert 12 == stats.nSolutions
    
    def test2(self):
        cp = makeSolver()
        x = makeIntVar(cp, -4, 7)

        b = isEqual(x, -2)

        cp.getStateManager().saveState()
        cp.post(equal(b, 1))
        assert -2 == x.min()
        cp.getStateManager().restoreState()

        cp.getStateManager().saveState()
        cp.post(equal(b, 0))
        assert x.contains(-2) == False
        cp.getStateManager().restoreState()
    
    def test3(self):
        cp = makeSolver()

        x1 = makeIntVar(cp, -4, 7)
        cp.post(equal(x1, -2))
        b1 = makeBoolVar(cp)
        cp.post(IsEqual(b1, x1, -2))
        assert b1.isTrue() == True

        x2 = makeIntVar(cp, -4, 7)
        b2 = makeBoolVar(cp)
        cp.post(IsEqual(b2, x2, -3))
        assert b2.isFalse() == False
    
    def test4(self):
        cp = makeSolver()
        x = makeIntVar(cp, -4, 7)
        b = makeBoolVar(cp)

        cp.getStateManager().saveState()
        cp.post(equal(b, 1))
        cp.post(IsEqual(b, x, -2))
        assert -2 == x.min()
        cp.getStateManager().restoreState()

        cp.getStateManager().saveState()
        cp.post(equal(b, 0))
        cp.post(IsEqual(b, x, -2))
        assert x.contains(-2) == False
        cp.getStateManager().restoreState()


