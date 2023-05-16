#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
A view on a variable of type a*x

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/24

'''
import math
from minicp.engine.core.int_var import IntVar
from minicp.exception.in_consistency_error import InconsistencyError

class IntVarViewMul(IntVar):
    
    def __init__(self, x, a):
        assert a > 0
        self.x = x
        self.a = a

    def getSolver(self):
        return self.x.getSolver()
    
    def whenFixed(self, f):
        self.x.whenFixed(f)

    def whenBoundChange(self, f):
        self.x.whenBoundChange(f)

    def whenDomainChange(self, f):
        self.x.whenDomainChange(f)

    def propagateOnDomainChange(self, c):
        self.x.propagateOnDomainChange(c)

    def propagateOnFix(self,  c):
        self.x.propagateOnFix(c)

    def propagateOnBoundChange(self, c):
        self.x.propagateOnBoundChange(c)

    def min(self):
        if self.a >= 0:
            return self.a * self.x.min()
        else:
            self.a * self.x.max()

    def max(self):
        if self.a >= 0:
            return self.a * self.x.max()
        else:
            return self.a * self.x.min()

    def size(self):
        return self.x.size()

    def fillArray(self, dest):
        raise NotImplementedError

    def isFixed(self):
        return self.x.isFixed()

    def contains(self, v):
        if v % self.a != 0:
            return False
        else:
            return self.x.contains(v / self.a)

    def remove(self, v):
        if v % self.a == 0:
            self.x.remove(v / self.a)

    def fix(self, v):
        if v % self.a == 0:
            self.x.fix(v / self.a)
        else:
            raise InconsistencyError("InconsistencyError")

    def removeBelow(self, v):
        self.x.removeBelow(math.ceil(v / self.a))

    def removeAbove(self, v):
        self.x.removeAbove(math.floor(v / self.a))
