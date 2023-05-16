#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Less or equal constraint between two variables (x <= y)

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/23

'''
from minicp.engine.core.constraint import Constraint
from minicp.engine.core.int_var_impl import IntVarImpl

class LessOrEqual(Constraint):
    
    def __init__(self, x: IntVarImpl, y: IntVarImpl):
        super().__init__(x.getSolver())
        self.x = x
        self.y = y

    def post(self):
        self.x.propagateOnBoundChange(self)
        self.y.propagateOnBoundChange(self)
        self.propagate()
    
    def propagate(self):
        self.x.removeAbove(self.y.max())
        self.y.removeBelow(self.x.min())
        if self.x.max() <= self.y.min():
            self.setActive(False)
    