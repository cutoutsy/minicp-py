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
from minicp.engine.constraints.less_or_equal import LessOrEqual
from minicp.exception import *

class TestLessOrEqual:

    def test1(self):
        cp = makeSolver()
        x = makeIntVar(cp, -5, 5)
        y = makeIntVar(cp, -10, 10)

        cp.post(LessOrEqual(x, y))

        assert -5 == y.min()

        y.removeAbove(3)
        cp.fixPoint()

        assert 9 == x.size()
        assert 3 == x.max()

        x.removeBelow(-4)
        cp.fixPoint()

        assert -4 == y.min()
    