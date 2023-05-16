#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Reified logical or constraint

// b <=> x1 or x2 or ... xn

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/24

'''
from typing import List

from minicp.engine.core.constraint import Constraint
from minicp.engine.core.int_var_impl import IntVarImpl
from minicp.engine.core.bool_var import BoolVar

class IsOr(Constraint):
    def __init__(self, b: BoolVar, x: List[BoolVar]):
        super().__init__(b.getSolver())
        self.b = b
        self.x = x
        self.n = len(x)
        or = new Or(x);

        nFreeVars = getSolver().getStateManager().makeStateInt(n);
        freeVarIndex = new int[n];
        for (int i = 0; i < n; i++) {
            freeVarIndex[i] = i;
        }
