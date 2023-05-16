#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/20

'''
from minicp.engine.core.constraint import Constraint
from minicp.engine.core.int_var_impl import IntVarImpl

class Equal(Constraint):
    
    def __init__(self, x: IntVarImpl, y: IntVarImpl):
        super().__init__(x.getSolver())
        self.x = x
        self.y = y
        self.domVal = None
    
    def whenDomainChange_x(self):
        self.boundsIntersect()
        self.pruneEquals(self.x, self.y, self.domVal)
    
    def whenDomainChange_y(self):
        self.boundsIntersect()
        self.pruneEquals(self.y, self.x, self.domVal)
    
    
    def post(self):
        if self.y.isFixed():
            self.x.fix(self.y.min())
        elif self.x.isFixed():
            self.y.fix(self.x.min())
        else:
            self.boundsIntersect()
            self.domVal = [0] * max(self.x.size(), self.y.size())
            self.pruneEquals(self.y, self.x, self.domVal)
            self.pruneEquals(self.x, self.y, self.domVal)
            self.x.whenDomainChange(self.whenDomainChange_x)
            self.y.whenDomainChange(self.whenDomainChange_y)

    def pruneEquals(self, from_, to, domVal):
        nVal = to.fillArray(domVal)
        for k in range(nVal):
            if not from_.contains(domVal[k]):
                to.remove(domVal[k])

    def boundsIntersect(self):
        # print("self x: ", self.x)
        # print("self y: ", self.y)
        newMin = max(self.x.min(), self.y.min())
        newMax = min(self.x.max(), self.y.max())
        # print("newMin: ", newMin, "newMax: ", newMax)
        self.x.removeBelow(newMin)
        self.x.removeAbove(newMax)
        self.y.removeBelow(newMin)
        self.y.removeAbove(newMax)
    
    def propagate(self):
        if self.y.isFixed():
            self.x.remove(self.y.min() + self.v)
        else:
            self.y.remove(self.x.min() - self.v)
        self.setActive(False)
    