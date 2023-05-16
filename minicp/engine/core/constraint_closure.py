#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2023 NetEase.com, Inc. All Rights Reserved.
# Copyright 2023, The Fuxi AI Lab.
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/25

'''
from minicp.engine.core.constraint import Constraint

class ConstraintClosure(Constraint):
    def __init__(self, cp, filtering):
        super().__init__(cp)
        self.filtering = filtering
    
    def post(self):
        pass

    def propagate(self):
        self.filtering()