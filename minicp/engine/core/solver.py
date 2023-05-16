#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/18

'''
from abc import ABCMeta, abstractmethod

class Solver(metaclass=ABCMeta):
    
    @abstractmethod
    def post(self, c):
        pass

    @abstractmethod
    def schedule(self, c):
        pass

    @abstractmethod
    def fixPoint(self):
        pass

    @abstractmethod
    def onFixPoint(listener):
        pass

    @abstractmethod
    def minimize(x):
        pass