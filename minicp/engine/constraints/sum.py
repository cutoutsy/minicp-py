#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Sum Constraint

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/23

'''
from typing import List

from minicp.engine.core.constraint import Constraint
from minicp.engine.core.int_var_impl import IntVarImpl
from minicp.engine.core.int_var_view_opposite import IntVarViewOpposite
from minicp.exception.in_consistency_error import InconsistencyError

class Sum(Constraint):
    
    def __init__(self, x: List[IntVarImpl], y):
        super().__init__(x[0].getSolver())
        self.x = x[:]
        self.n = len(x) + 1
        self.min = [0] * (len(x) + 1)
        self.max = [0] * (len(x) + 1)
        self.nFixed = super().getSolver().getStateManager().makeStateInt(0)
        self.sumFixed = super().getSolver().getStateManager().makeStateRef(0)
        self.fixed = list(range(0, self.n))
        
        if isinstance(y, int):
            self.x.append(IntVarImpl(super().getSolver(), -y, -y))
        else:
            self.x.append(IntVarViewOpposite(y))
    
    def post(self):
        for var in self.x:
            var.propagateOnBoundChange(self)
        self.propagate()
    
    def propagate(self):
        # Filter the unfixed vars and update the partial sum
        nF = self.nFixed.value()
        sumMin = self.sumFixed.value()
        sumMax = self.sumFixed.value()
        # iterate over not-fixed variables and update partial sum
        # if one variable is detected as fixed
        for i in range(nF, len(self.x)):
        # for (int i = nF; i < x.length; i++) {
            idx = self.fixed[i]
            self.min[idx] = self.x[idx].min()
            self.max[idx] = self.x[idx].max()
            sumMin += self.min[idx]  # Update partial sum
            sumMax += self.max[idx]
            if self.x[idx].isFixed():
                self.sumFixed.setValue(self.sumFixed.value() + self.x[idx].min());
                self.fixed[i] = self.fixed[nF]; # Swap the variables
                self.fixed[nF] = idx
                nF += 1

        # print("sumMin: ", sumMin, "sumMax: ", sumMax)
        self.nFixed.setValue(nF)
        if sumMin > 0 or sumMax < 0: 
            raise InconsistencyError("InconsistencyError")
        # iterate over not-fixed variables
        for i in range(nF, len(self.x)):
            idx = self.fixed[i]
            # print("sumMin - self.min[idx]: ", sumMin - self.min[idx])
            self.x[idx].removeAbove(-(sumMin - self.min[idx]))
            # print("sumMax - self.max[idx]: ", sumMax - self.max[idx])
            self.x[idx].removeBelow(-(sumMax - self.max[idx]))