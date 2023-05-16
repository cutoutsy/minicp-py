#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/20

'''
from minicp.engine.core.constraint import Constraint

class EqualNum(Constraint):
    
    def __init__(self, x, v):
        super().__init__(x.getSolver())
        self.x = x
        self.v = v
    
    def post(self):
        self.x.fix(self.v)
