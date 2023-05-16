#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/05/08

'''

class TrailStateEntry:
    def __init__(self, v, copy):
        self.v = v
        self.copy = copy
    
    def restore(self):
        self.copy.v = self.v

class Trail:

    def __init__(self, trail, initial):
        self.trail = trail
        self.v = initial
        self.lastMagic = self.trail.getMagic() - 1
    
    def __trail(self):
        trailMagic = self.trail.getMagic()
        if self.lastMagic != trailMagic:
            self.lastMagic = trailMagic
            self.trail.pushState(TrailStateEntry(self.v, self))

    def setValue(self, v):
        if v != self.v:
            self.__trail()
            self.v = v
        return self.v
    
    def value(self):
        return self.v
    
    def __str__(self):
        return "" + str(self.v)
    
    def increment(self):
        self.setValue(self.v + 1)

    def decrement(self):
        self.setValue(self.v - 1)