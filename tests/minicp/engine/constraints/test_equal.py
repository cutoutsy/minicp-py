#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/27

'''
import sys
import pytest
from minicp.engine.core.minicp import MiniCP
from minicp.state.copier import Copier
from minicp.cp.factory import *
from minicp.cp.branch_schema import *

class TestEqual:

    def equalDom(self, x, y):
        for v in range(x.min(), x.max()):
            if x.contains(v) and not y.contains(v):
                return False
        for v in range(y.min(), y.max()):
            if y.contains(v) and not x.contains(v):
                return False
        return True

    def testEqual1(self):
        cp = makeSolver()
        x = makeIntVar(cp, 0, 10)
        y = makeIntVar(cp, 0, 10)

        cp.post(equal(x,y))

        x.removeAbove(7)
        cp.fixPoint()

        assert self.equalDom(x,y) == True

        y.removeAbove(6)
        cp.fixPoint()

        x.remove(3)
        cp.fixPoint()

        assert self.equalDom(x,y) == True

        x.fix(1)
        cp.fixPoint()

        assert self.equalDom(x,y) == True

    
    def testEqual2(self):
        cp = makeSolver()
        x = makeIntVar(cp, sys.maxsize - 20, sys.maxsize -1)
        y = makeIntVar(cp, sys.maxsize - 10, sys.maxsize -1)
        
        cp.post(notEqual(x, sys.maxsize - 5))

        cp.post(equal(x,y))

        cp.post(equal(x, sys.maxsize - 1))

        assert y.min() == (sys.maxsize - 1)
