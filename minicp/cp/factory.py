#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Factory to create Solver, IntVar, Constraint and 
some modeling utility methods.

Authors: cutoutsy(cutoutsy@corp.netease.com)
Date: 2023/04/25

'''
from typing import List

from minicp.engine.core.minicp import MiniCP
from minicp.state.copier import Copier
from minicp.state.trailer import Trailer
from minicp.engine.core.int_var_impl import IntVarImpl
from minicp.engine.core.bool_var_impl import BoolVarImpl
from minicp.engine.constraints.sum import Sum
from minicp.engine.core.int_var_view_mul import IntVarViewMul
from minicp.engine.core.int_var_view_opposite import IntVarViewOpposite
from minicp.engine.constraints.maximum import Maximum
from minicp.engine.constraints.is_less_or_equal import IsLessOrEqual
from minicp.engine.constraints.is_equal import IsEqual
from minicp.search.dfsearch import DFSearch
from minicp.engine.constraints.equal_num import EqualNum
from minicp.engine.constraints.not_equal_num import NotEqualNum
from minicp.engine.constraints.equal import Equal
from minicp.engine.constraints.not_equal import NotEqual
from minicp.engine.constraints.less_or_equal import LessOrEqual
from minicp.engine.core.int_var_view_offset import IntVarViewOffset


def makeSolver():
    """
    Creates a constraint programming solver
    """
    # return MiniCP(Copier())
    return MiniCP(Trailer())

def makeDfs(cp, branching):
    return DFSearch(cp.getStateManager(), branching);

def makeIntVar(cp, min, max):
    return IntVarImpl(cp, min, max)

def makeBoolVar(cp):
    tmp = IntVarImpl(cp, 0, 1)
    return BoolVarImpl(tmp)

def plus(x, v):
    return x if v == 0 else IntVarViewOffset(x, v)

def minus(x, v=None):
    if v is None:
        return IntVarViewOpposite(x)
    else:
        return IntVarViewOffset(x, -v)

def sum_list(*args):
    sumMin = 0
    sumMax = 0
    x = []
    for arg in args:
        sumMin += arg.min()
        sumMax += arg.max()
        x.append(arg)
    cp = args[0].getSolver()
    # print("sumMin: ", sumMin, " sumMax: ", sumMax)
    s = makeIntVar(cp, sumMin, sumMax)
    cp.post(Sum(x, s))
    return s

def sum_c(y, x: List[IntVarImpl]):
    return Sum(x, y)

def mul(x, a):
    if a == 0:
        return IntVarImpl(x.getSolver(), 0, 0)
    elif a == 1:
        return x
    elif a < 0:
        return IntVarViewOpposite((IntVarViewMul(x, -a)))
    else:
        return IntVarViewMul(x, a)

def equal(x, v):
    if isinstance(v, int):
        return EqualNum(x, v)
    else:
        return Equal(x, v)

def notEqual(x, y, v=0):
    if isinstance(y, int):
        return NotEqualNum(x, y)
    else:
        return NotEqual(x, y, v)

def maximum(x):
    cp = x[0].getSolver()
    min_x = min([ele.min() for ele in x])
    max_x = max([ele.max() for ele in x])
    y = makeIntVar(cp, min_x, max_x)
    cp.post(Maximum(x, y))
    return y

def minimum(x):
    return minus(maximum([minus(x_) for x_ in x]))

def isEqual(x, c):
    b = makeBoolVar(x.getSolver())
    cp = x.getSolver()
    try:
        cp.post(IsEqual(b, x, c))
    except Exception as e:
        print("factory isEqual error.")
        e.printStackTrace()
    return b

def isLessOrEqual(x, c):
    b = makeBoolVar(x.getSolver())
    cp = x.getSolver()
    cp.post(IsLessOrEqual(b, x, c))
    return b

def isLargerOrEqual(x, c):
    return isLessOrEqual(minus(x), -c)

def isLarger(x, c):
    return isLargerOrEqual(x, c + 1)

def lessOrEqual(x, y):
    return LessOrEqual(x, y)

def largeOrEqual(x, y):
    return LessOrEqual(y, x)