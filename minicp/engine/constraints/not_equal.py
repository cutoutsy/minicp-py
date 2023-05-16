#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/18

'''
from minicp.engine.core.constraint import Constraint
from minicp.engine.core.int_var_impl import IntVarImpl

class NotEqual(Constraint):
    def __init__(self, x: IntVarImpl, y: IntVarImpl, v=0):
        super().__init__(x.getSolver())
        self.x = x
        self.y = y
        self.v = v
        self.scheduled = False
    
    def post(self):
        if self.y.isFixed():
            self.x.remove(self.y.min() + self.v)
        elif self.x.isFixed():
            self.y.remove(self.x.min() - self.v)
        else:
            self.x.propagateOnFix(self)
            self.y.propagateOnFix(self)
    
    def propagate(self):
        # print("not equal propagate.")
        if self.y.isFixed():
            self.x.remove(self.y.min() + self.v)
        else:
            self.y.remove(self.x.min() - self.v)
        self.setActive(False)
