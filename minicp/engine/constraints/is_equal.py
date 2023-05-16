#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Reified equality constraint

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/25

'''
from minicp.engine.core.constraint import Constraint
from minicp.engine.core.int_var import IntVar
from minicp.engine.core.bool_var import BoolVar

class IsEqual(Constraint):
    def __init__(self, b: BoolVar, x: IntVar, v):
        super().__init__(b.getSolver())
        self.b = b
        self.x = x
        self.v = v
    
    def whenFixedCall(self):
        if self.b.isTrue():
            self.x.removeAbove(self.v)
        else:
            self.x.removeBelow(self.v + 1)
    
    def whenBoundChangeCall(self):
        if self.x.max() <= self.v:
            self.b.fix(1)
        elif self.x.min() > self.v:
            self.b.fix(0)

    def post(self):
        self.propagate()
        if self.isActive():
            self.x.propagateOnDomainChange(self)
            self.b.propagateOnFix(self)
    
    def propagate(self):
        if self.b.isTrue():
            self.x.fix(self.v)
            self.setActive(False)
        elif self.b.isFalse():
            self.x.remove(self.v)
            self.setActive(False)
        elif not self.x.contains(self.v):
            self.b.fix(0)
            self.setActive(False)
        elif self.x.isFixed():
            self.b.fix(1)
            self.setActive(False)