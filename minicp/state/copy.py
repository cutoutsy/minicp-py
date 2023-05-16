#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/20

'''

class CopyStateEntry:
    def __init__(self, v, copy):
        self.v = v
        self.copy = copy
    
    def restore(self):
        self.copy.v = self.v

class Copy:

    def __init__(self, initial):
        self.v = initial
    
    def setValue(self, v):
        self.v = v
        return v
    
    def value(self):
        return self.v
    
    def save(self):
        return CopyStateEntry(self.v, self)
    
    def increment(self):
        self.v += 1

    def decrement(self):
        self.v -= 1