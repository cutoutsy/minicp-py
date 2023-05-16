#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/24

'''
from minicp.engine.core.bool_var import BoolVar
from minicp.engine.core.int_var import IntVar
from minicp.engine.core.int_var_impl import IntVarImpl

class BoolVarImpl(BoolVar):
    
    def __init__(self, binaryVar: IntVar):
        super().__init__()
        if binaryVar.max() > 1 or binaryVar.min() < 0:
            raise ValueError("must be a binary {0,1} variable")
        self.binaryVar = binaryVar
    
    def isTrue(self):
        return self.binaryVar.min() == 1
    
    def isFalse(self):
        return self.binaryVar.max() == 0
    
    def fix(self, b):
        self.binaryVar.fix(int(b))
    
    def getSolver(self):
        return self.binaryVar.getSolver()

    def whenFixed(self, f):
        self.binaryVar.whenFixed(f)

    def whenBoundChange(self, f):
        self.binaryVar.whenBoundChange(f)

    def whenDomainChange(self, f):
        self.binaryVar.whenDomainChange(f)

    def propagateOnDomainChange(self, c):
        self.binaryVar.propagateOnDomainChange(c)

    def propagateOnFix(self, c):
        self.binaryVar.propagateOnFix(c)

    def propagateOnBoundChange(self, c):
        self.binaryVar.propagateOnBoundChange(c)

    def min(self):
        return self.binaryVar.min()

    def max(self):
        return self.binaryVar.max()

    def size(self):
        return self.binaryVar.size()

    def fillArray(dest):
        raise NotImplementedError

    def isFixed(self):
        return self.binaryVar.isFixed()

    def contains(self, v):
        return self.binaryVar.contains(v)

    def remove(self, v):
        self.binaryVar.remove(v)
    
    def removeBelow(self, v):
        self.binaryVar.removeBelow(v)

    def removeAbove(self, v):
        self.binaryVar.removeAbove(v)
    
    def __str__(self):
        if self.isTrue():
            return "true"
        elif self.isFalse():
            return "false"
        return "{false,true}"
    
