#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Generic Stack that can be saved and restored through StateManager

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/23

'''
from minicp.state.state_manager import StateManger

class StateStack:
    
    def __init__(self, sm):
        self.size = sm.makeStateInt(0)
        self.stack = []
    
    def push(self, elem):
        self.stack.append(elem)
        self.size.increment()

    # def size(self):
        # print("state stack size run...")
        # return self.size.value()
    
    def __len__(self):
        return self.size.value()
    
    def get(self, index):
        return self.stack[index]