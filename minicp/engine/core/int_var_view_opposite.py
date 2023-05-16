#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 A view on a variable of type -x

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/24

'''
from minicp.engine.core.int_var import IntVar

class IntVarViewOpposite(IntVar):
    
    def __init__(self, x):
        self.x = x

    def getSolver(self):
        return self.x.getSolver()
    
    def whenFixed(self, f):
        self.x.whenFixed(f);

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
        return -self.x.max()

    def max(self):
        return -self.x.min()

    def size(self):
        return self.x.size()

    def fillArray(self, dest):
        raise NotImplementedError

    def isFixed(self):
        return self.x.isFixed()

    def contains(self, v):
        return self.x.contains(-v)

    def remove(self, v):
        self.x.remove(-v)

    def fix(self, v):
        self.x.fix(-v)

    def removeBelow(self, v):
        self.x.removeAbove(-v)

    def removeAbove(self, v):
        self.x.removeBelow(-v)
