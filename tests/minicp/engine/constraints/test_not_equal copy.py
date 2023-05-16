#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/27

'''
import pytest
from minicp.engine.core.minicp import MiniCP
from minicp.state.copier import Copier
from minicp.cp.factory import *
from minicp.cp.branch_schema import *

class TestNotEqual:

    def test1(self):
        cp = makeSolver()
        
        x = makeIntVar(cp, 0, 9)
        y = makeIntVar(cp, 0, 9)

        cp.post(notEqual(x, y))

        cp.post(equal(x, 6))

        assert y.contains(6) == False
        assert 9 == y.size()