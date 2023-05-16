#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/24

'''
from minicp.engine.core.int_var import IntVar

class IntVarViewOffset(IntVar):
    
    def __init__(self, x, offset):
        self.x = x
        self.o = offset

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
        return self.x.min() + self.o

    def max(self):
        return self.x.max() + self.o

    def size(self):
        return self.x.size()

    def fillArray(self, dest):
        raise NotImplementedError

    def isFixed(self):
        return self.x.isFixed()

    def contains(self, v):
        return self.x.contains(v - self.o)

    def remove(self, v):
        self.x.remove(v - self.o)

    def fix(self, v):
        self.x.fix(v - self.o)

    def removeBelow(self, v):
        self.x.removeAbove(v - self.o)

    def removeAbove(self, v):
        self.x.removeBelow(v - self.o)
