#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/25

'''
import pytest

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
from minicp.engine.constraints.maximum import Maximum
from minicp.cp.factory import *

class TestMaximum:

    def test1(self):
        cp = makeSolver()
        x = []
        for _ in range(3):
            x.append(makeIntVar(cp, 0, 9))
        y = makeIntVar(cp, -5, 20)
        cp.post(Maximum(x, y));

        assert 9 == y.max()
        assert 0 == y.min()

        y.removeAbove(8)
        cp.fixPoint()

        assert 8 == x[0].max()
        assert 8 == x[1].max()
        assert 8 == x[2].max()

        y.removeBelow(5)
        x[0].removeAbove(2)
        x[1].removeBelow(6)
        x[2].removeBelow(6)
        cp.fixPoint()

        assert 8 == y.max()
        assert 6 == y.min()

        y.removeBelow(7)
        x[1].removeAbove(6)
        # x0 = 0..2
        # x1 = 6
        # x2 = 6..8
        # y = 7..8
        cp.fixPoint()
        assert 7 == x[2].min()
    
    def test2(self):
        cp = makeSolver()
        x1 = makeIntVar(cp, 0, 0)
        x2 = makeIntVar(cp, 1, 1)
        x3 = makeIntVar(cp, 2, 2)
        y = maximum([x1, x2, x3])

        assert 2 == y.max()
    
    def test3(self):
        cp = makeSolver()
        x1 = makeIntVar(cp, 0, 10)
        x2 = makeIntVar(cp, 0, 10)
        x3 = makeIntVar(cp, -5, 50)
        y = maximum([x1, x2, x3])

        y.removeAbove(5)
        cp.fixPoint()

        assert 5 == x1.max()
        assert 5 == x2.max()
        assert 5 == x3.max()
    
    def test4(self):
        cp = makeSolver()
        x = []
        for _ in range(4):
            x.append(makeIntVar(cp, 0, 4))
        y = makeIntVar(cp, -5, 20)

        allIntVars = x[:]
        allIntVars.append(y)

        def branching():
            idx = -1
            for k in range(len(allIntVars)):
                if allIntVars[k].size() > 1:
                    idx = k
                    break
            if idx == -1:
                return []
            else:
                qi = allIntVars[idx]
                v = qi.min()
                def left():
                    cp.post(EqualNum(qi, v))
                def right():
                    cp.post(NotEqualNum(qi, v))
                return [left, right]

        dfs = DFSearch(cp.getStateManager(), branching)

        cp.post(Maximum(x, y))

        stats = dfs.solve()
        assert stats.nSolutions == 625

    def test5(self):
        cp = makeSolver()
        x = []
        for _ in range(3):
            x.append(makeIntVar(cp, 0, 9))
        y = makeIntVar(cp, -5, 20);
        cp.post(Maximum(x, y))

        assert 9 == y.max()
        assert 0 == y.min()

        x[0].removeAbove(3)
        y.removeBelow(6)
        cp.fixPoint()

        assert 6 == y.min()
        assert 9 ==  y.max()
        assert 0 == x[1].min()
        assert 0 == x[2].min()

        