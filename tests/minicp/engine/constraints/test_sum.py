#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/28

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
from minicp.engine.constraints.sum import Sum
from minicp.exception import *

class TestSum:

    def test1(self):
        cp = makeSolver()
        y = makeIntVar(cp, -100, 100)
        x = [makeIntVar(cp, 0, 5), makeIntVar(cp, 1, 5), makeIntVar(cp, 0, 5)]
        cp.post(Sum(x, y))

        assert 1 == y.min()
        assert 15 == y.max()
    
    def test2(self):
        cp = makeSolver()
        x = [makeIntVar(cp, -5, 5), makeIntVar(cp, 1, 2), makeIntVar(cp, 0, 1)]
        y = makeIntVar(cp, 0, 100)
        cp.post(Sum(x, y))

        assert -3 == x[0].min()
        assert 0 == y.min()
        assert 8 == y.max()
    
    def test3(self):
        cp = makeSolver()
        x = [makeIntVar(cp, -5, 5), makeIntVar(cp, 1, 2), makeIntVar(cp, 0, 1)]
        # IntVar[] x = new IntVar[]{makeIntVar(cp, -5, 5), makeIntVar(cp, 1, 2), makeIntVar(cp, 0, 1)}
        y = makeIntVar(cp, 5, 5)
        cp.post(Sum(x, y))

        x[0].removeBelow(1)
        # 1-5 + 1-2 + 0-1 = 5
        x[1].fix(1)
        # 1-5 + 1 + 0-1 = 5
        cp.fixPoint()

        assert 4 == x[0].max()
        assert 3 == x[0].min()
        assert 1 == x[2].max()
        assert 0 == x[2].min()
    
    def test4(self):
        cp = makeSolver()
        x = [makeIntVar(cp, 0, 5), makeIntVar(cp, 0, 2), makeIntVar(cp, 0, 1)]
        cp.post(Sum(x, 0))

        assert 0 == x[0].max()
        assert 0 == x[1].max()
        assert 0 == x[2].max()

    def test5(self):
        cp = makeSolver()
        x = [makeIntVar(cp, -5, 0), makeIntVar(cp, -5, 0), makeIntVar(cp, -3, 0)]
        cp.post(Sum(x, 0))

        assert 0 == x[0].min()
        assert 0 == x[1].min()
        assert 0 == x[2].min()
    
    def test6(self):
        cp = makeSolver()
        x = [makeIntVar(cp, -5, 0), makeIntVar(cp, -5, 0), makeIntVar(cp, -3, 3)]
        cp.post(Sum(x, 0))
        assert -3 == x[0].min()
        assert -3 == x[1].min()

        x[2].removeAbove(0)
        cp.fixPoint()

        assert 0 == x[0].min()
        assert 0 == x[1].min()
        assert 0 == x[2].min()
    
    def test7(self):
        cp = makeSolver()
        x = [makeIntVar(cp, -5, 0), makeIntVar(cp, -5, 0), makeIntVar(cp, -3, 3)]
        cp.post(Sum(x, 0))
        assert -3 == x[0].min()
        assert -3 == x[1].min()

        x[2].remove(1)
        x[2].remove(2)
        x[2].remove(3)
        x[2].remove(4)
        x[2].remove(5)
        cp.fixPoint()

        assert 0 == x[0].min()
        assert 0 == x[1].min()
        assert 0 == x[2].min()
    
    def test8(self):
        cp = makeSolver()
        x = [makeIntVar(cp, -3, 3), makeIntVar(cp, -3, 3), makeIntVar(cp, -3, 3)]
        cp.post(Sum(x, 0))

        search = makeDfs(cp, firstFail(x))

        stats = search.solve()

        assert 37 == stats.nSolutions
    
    def test9(self):
        cp = makeSolver()
        x = [makeIntVar(cp, -9, -9)]
        failed = False
        try:
            cp.post(Sum(x, 0))
        except InconsistencyError:
            failed = True
        assert failed == True
    
    def test10(self):
        cp = makeSolver()
        x = [makeIntVar(cp, -9, -4)]
        failed = False
        try:
            cp.post(Sum(x, 0))
        except InconsistencyError:
            failed = True
        assert failed == True

    