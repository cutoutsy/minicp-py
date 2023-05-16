#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/18

'''
from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):
    
    @abstractmethod
    def setValue(v):
        pass
    
    @abstractmethod
    def value():
        pass