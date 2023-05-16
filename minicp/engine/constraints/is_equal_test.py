#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2023 NetEase.com, Inc. All Rights Reserved.
# Copyright 2023, The Fuxi AI Lab.
'''
Reified equality constraint

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/25

'''
from minicp.engine.core.constraint import Constraint
from minicp.engine.core.int_var import IntVar
from minicp.engine.core.bool_var import BoolVar

class IsEqualTest(Constraint):
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
            # self.x.propagateOnDomainChange(self)
            self.b.propagateOnFix(self)
    
    def propagate(self):
        if self.b.isTrue():
            self.x.fix(self.v)
            self.setActive(False)