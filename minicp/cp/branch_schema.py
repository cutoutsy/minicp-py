#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Factory for search procedures.
A typical custom search on an array of variable

Authors: cutoutsy(cutoutsy@corp.netease.com)
Date: 2023/04/27

'''
from minicp.engine.constraints.not_equal_num import NotEqualNum
from minicp.engine.constraints.equal_num import EqualNum

def firstFail(x):
    def f():
        xs = None
        max_size = 0
        choice_idx = -1
        for idx, var in enumerate(x):
            if var.size() > 1:
                if var.size() > max_size:
                    max_size = var.size()
                    xs = var
                    choice_idx = idx
        if xs is None:
            return []
        else:
            v = xs.max()
            def left():
                xs.getSolver().post(EqualNum(xs, v))
            def right():
                xs.getSolver().post(NotEqualNum(xs, v))
            return [left, right]
    return f