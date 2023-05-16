#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/18

'''
from minicp.engine.core.int_domain import IntDomain
from minicp.state.state_sparse_set import StateSparseSet

class SparseSetDomain(IntDomain):

    def __init__(self, sm, min, max):
        super().__init__()
        self.domain = StateSparseSet(sm, max - min + 1, min)
    
    def min(self):
        return self.domain.min()
    
    def max(self):
        return self.domain.max()
    
    def size(self):
        return self.domain.size()
    
    def contains(self, v):
        return self.domain.contains(v)
    
    def isSingleton(self):
        return self.domain.size() == 1
    
    def remove(self, v, l):
        if self.domain.contains(v):
            maxChanged = self.max() == v
            minChanged = self.min() == v
            self.domain.remove(v)
            if self.domain.size() == 0:
                l.empty()
            l.change()
            if maxChanged:
                l.changeMax()
            if minChanged:
                l.changeMin()
            if self.domain.size() == 1:
                l.fix()
    
    def removeAllBut(self, value, l):
        if self.domain.contains(value):
            if self.domain.size() != 1:
                maxChanged = self.max() != value
                minChanged = self.min() != value
                self.domain.removeAllBut(value)
                if self.domain.size() == 0:
                    l.empty()
                l.fix()
                l.change()
                if maxChanged:
                    l.changeMax()
                if minChanged:
                    l.changeMin()
        else:
            self.domain.removeAll()
            l.empty()
    
    def removeAbove(self, value, l):
        if self.domain.max() > value:
            self.domain.removeAbove(value)
            if self.domain.size() == 0:
                l.empty()
            elif self.domain.size() == 1:
                l.fix()
                l.changeMax()
                l.change()
            else:
                l.changeMax()
                l.change()

    def removeBelow(self, value, l):
        if self.domain.min() < value:
            self.domain.removeBelow(value)
            if self.domain.size() == 0:
                l.empty()
            elif self.domain.size() == 1:
                l.fix()
                l.changeMin()
                l.change()
            else:
                l.changeMin()
                l.change()
    
    def fillArray(self, dest):
        return self.domain.fillArray(dest)
    
    def __str__(self) -> str:
        if self.size() == 0:
            return "{}"
        vals = []
        for i in range(self.min(), self.max() + 1):
            if self.contains(i):
                vals.append(i)
        return '{' + ','.join([str(v) for v in vals]) + '}'
    
