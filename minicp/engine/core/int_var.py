#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/18

'''
# from abc import ABCMeta, abstractmethod

class IntVar:
    
    # @abstractmethod
    def getSolver(self):
        pass

    # @abstractmethod
    def whenFixed(self, f):
        pass

    # @abstractmethod
    def whenBoundChange(self, f):
        pass

    # @abstractmethod
    def whenDomainChange(self, f):
        pass

    # @abstractmethod
    def propagateOnDomainChange(self, c):
        pass

    # @abstractmethod
    def propagateOnFix(c):
        pass

    # @abstractmethod
    def propagateOnBoundChange(self, c):
        pass

    # @abstractmethod
    def min(self):
        pass

    # @abstractmethod
    def max(self):
        pass

    # @abstractmethod
    def size(self):
        pass
    
    # @abstractmethod
    def fillArray(self, dest):
        pass
    
    # @abstractmethod
    def isFixed(self):
        pass

    # @abstractmethod
    def contains(self, v):
        pass
    
    # @abstractmethod
    def remove(self, v):
        pass

    # @abstractmethod
    def fix(self, v):
        pass

    # @abstractmethod
    def removeBelow(self, v):
        pass

    # @abstractmethod
    def removeAbove(self, v):
        pass

