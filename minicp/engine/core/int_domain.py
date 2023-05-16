#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/18

'''
from abc import ABCMeta, abstractmethod

class IntDomain(metaclass=ABCMeta):
    
    @abstractmethod
    def min(self):
        pass
    
    @abstractmethod
    def max(self):
        pass
    
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def contains(self, v):
        pass

    @abstractmethod
    def isSingleton(self):
        pass
    
    @abstractmethod
    def remove(self, v, l):
        pass
    
    @abstractmethod
    def removeAllBut(self, v, l):
        pass
    
    @abstractmethod
    def removeBelow(self, v, l):
        pass
    
    @abstractmethod
    def removeAbove(self, v, l):
        pass
    
    @abstractmethod
    def fillArray(self, dest):
        pass