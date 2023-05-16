#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/05/08

'''
from minicp.state.state_manager import StateManger
from minicp.state.trail import Trail



class Trailer(StateManger):
    
    def __init__(self):
        super().__init__()
        self.prior = []
        self.current = []
        self.magic = 0
    
    def onRestore(self, listener):
        return super().onRestore(listener)

    def getMagic(self):
        return self.magic
    
    def pushState(self, entry):
        self.current.append(entry)

    def getLevel(self):
        return len(self.prior) - 1
    
    def saveState(self):
        self.prior.append(self.current)
        self.current = []
        self.magic += 1

    def restoreState(self):
        while len(self.current) != 0:
            se = self.current.pop()
            se.restore()
        self.current = self.prior.pop()
        self.magic += 1

    def withNewState(self):
        level = self.getLevel()
        self.saveState()
        return level

    def restoreStateUntil(self, level):
        while self.getLevel() > level:
            self.restoreState()
    
    def makeStateRef(self, initValue):
        r = Trail(self, initValue)
        return r
    
    def makeStateInt(self, initValue):
        s = Trail(self, initValue)
        return s
    
    def makeStateMap(self):
        return super().makeStateMap()

