#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/18

'''
from minicp.state.state_manager import StateManger
from minicp.exception.no_such_element_error import NoSuchElementError

class StateSparseSet:
    
    def __init__(self, sm, n, ofs):
        self.values = [i for i in range(n)]
        self.indexes = [i for i in range(n)]
        self.size_ = sm.makeStateInt(n)
        self.min_ = sm.makeStateInt(0)
        self.max_ = sm.makeStateInt(n - 1)
        self.ofs = ofs
        self.n = n

    def exchangePosition(self, val1, val2):
        v1 = val1
        v2 = val2
        i1 = self.indexes[v1]
        i2 = self.indexes[v2]
        self.values[i1] = v2
        self.values[i2] = v1
        self.indexes[v1] = i2
        self.indexes[v2] = i1

    def toArray(self):
        res = [0] * self.size()
        self.fillArray(res)
        return res
    
    def fillArray(self, dest):
        s = self.size_.value()
        for i in range(0, s):
            dest[i] = self.values[i] + self.ofs
        return s
    
    def isEmpty(self):
        return self.size_.value() == 0

    def size(self):
        return self.size_.value()
    
    def min(self):
        if self.isEmpty():
            raise NoSuchElementError("NoSuchElement")
        return self.min_.value() + self.ofs
    
    def max(self):
        if self.isEmpty():
            raise NoSuchElementError("NoSuchElement")
        return self.max_.value() + self.ofs
    
    def contains(self, val):
        val -= self.ofs
        if val < 0 or val >= self.n:
            return False
        else:
            return self.indexes[val] < self.size()

    def internalContains(self, val):
        if val < 0 or val >= self.n:
            return False
        else:
            return self.indexes[val] < self.size()

    def updateBoundsValRemoved(self, val):
        self.updateMaxValRemoved(val)
        self.updateMinValRemoved(val)
    
    def updateMinValRemoved(self, val):
        if not self.isEmpty() and self.min_.value() == val:
            for v in range(val + 1, self.max_.value() + 1):
                if self.internalContains(v):
                    self.min_.setValue(v)
                    return

    def updateMaxValRemoved(self, val):
        if not self.isEmpty() and self.max_.value() == val:
            for v in range(val - 1, self.min_.value() - 1, -1):
                if self.internalContains(v):
                    self.max_.setValue(v)
                    return
    
    def remove(self, val):
        if not self.contains(val):
            return False
        val -= self.ofs
        s = self.size()
        self.exchangePosition(val, self.values[s-1])
        self.size_.decrement()
        self.updateBoundsValRemoved(val)
        return True
    
    def removeAllBut(self, v):
        assert self.contains(v)
        v -= self.ofs
        val = self.values[0]
        index = self.indexes[v]
        self.indexes[v] = 0
        self.values[0] = v
        self.indexes[val] = index
        self.values[index] = val
        self.min_.setValue(v)
        self.max_.setValue(v)
        self.size_.setValue(1)
    
    def removeAll(self):
        self.size_.setValue(0)

    def removeBelow(self, value):
        if self.max() < value:
            self.removeAll()
        else:
            for v in range(self.min(), value):
                self.remove(v)
    
    def removeAbove(self, value):
        if self.min() > value:
            self.removeAll()
        else:
            max_ = self.max()
            for v in range(max_, value, -1):
                self.remove(v)