#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Maximum Constraint

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/25

'''
from typing import List

from minicp.engine.core.constraint import Constraint
from minicp.engine.core.int_var_impl import IntVarImpl

class Maximum(Constraint):
    
    def __init__(self, x: List[IntVarImpl], y: IntVarImpl):
        super().__init__(x[0].getSolver())
        assert len(x) > 0
        self.x = x
        self.y = y

    def post(self):
        for var in self.x:
            var.propagateOnBoundChange(self)
        self.y.propagateOnBoundChange(self)
        self.propagate()
    
    def propagate(self):
        var_active = []
        for var in self.x:
            var.removeAbove(self.y.max())
            if var.max() >= self.y.min():
                var_active.append(var)
        if len(var_active) == 1:
            var_active[0].removeBelow(self.y.min())

        
        max_max = -1
        min_max = -1
        for var in self.x:
            max_max = max(max_max, var.max())
            min_max = max(min_max, var.min())
        
        self.y.removeAbove(max_max)
        self.y.removeBelow(min_max)
    