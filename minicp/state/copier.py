#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/19

'''
from minicp.state.state_manager import StateManger
from minicp.state.copy import Copy



class Copier(StateManger):
    
    def __init__(self):
        super().__init__()
        self.store = []
        self.prior = []
    
    def onRestore(self, listener):
        return super().onRestore(listener)

    def getLevel(self):
        return len(self.prior) - 1
    
    def saveState(self):
        # print("saveState process...")
        self.prior.append([ele.save() for ele in self.store])

    def restoreState(self):
        store_copy = self.prior.pop()
        for se in store_copy:
            se.restore()

    def withNewState(self):
        level = self.getLevel()
        self.saveState()
        return level

    def restoreStateUntil(self, level):
        while self.getLevel() > level:
            self.restoreState()
    
    def makeStateRef(self, initValue):
        r = Copy(initValue)
        self.store.append(r)
        return r
    
    def makeStateInt(self, initValue):
        s = Copy(initValue)
        self.store.append(s)
        return s
    
    def makeStateMap(self):
        return super().makeStateMap()

