#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/18

'''

class Constraint:
    
    def __init__(self, cp):
        self.cp = cp
        self.active = cp.getStateManager().makeStateRef(True)
        self.scheduled = False

    def post(self):
        pass

    def getSolver(self):
        return self.cp
    
    def propagate(self):
        pass
    
    def setScheduled(self, scheduled):
        self.scheduled = scheduled
    
    def isScheduled(self):
        return self.scheduled
    
    def setActive(self, active):
        self.active.setValue(active)
    
    def isActive(self):
        return self.active.value()