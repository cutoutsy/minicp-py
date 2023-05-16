#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Boolean variable, that can be used as a 0-1 IntVar
0 corresponds to false, and 1 corresponds to true

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/24

'''
from minicp.engine.core.int_var import IntVar

class BoolVar(IntVar):

    def isTrue(self):
        pass

    def isFalse(self):
        pass
    
    def fix(self, b):
        pass