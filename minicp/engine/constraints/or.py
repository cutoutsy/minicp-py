#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Logical or constraint {x1 or x2 or ... xn}

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/24

'''
from typing import List

from minicp.engine.core.constraint import Constraint
from minicp.engine.core.bool_var import BoolVar

class Or(Constraint):
    def __init__(self, x: List[BoolVar]):
        super().__init__(x[0].getSolver())
        self.x = x
        self.n = len(x)
        wL = super().getSolver().getStateManager().makeStateInt(0)
        wR = super().getSolver().getStateManager().makeStateInt(self.n - 1)
    
    def post(self):
        self.propagate()


    def propagate(self):
        # update watched literals
        # TODO: implement the filtering using watched literal technique and make sure you pass all the tests
        # throw new NotImplementedException("Or")
        raise NotImplementedError("Or")