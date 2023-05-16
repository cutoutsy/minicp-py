#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2023 NetEase.com, Inc. All Rights Reserved.
# Copyright 2023, The Fuxi AI Lab.
'''
desc

Authors: cutoutsy(cutoutsy@gamil.com)
Date: 2023/04/18

'''
from abc import ABCMeta, abstractmethod

class StateManger(metaclass=ABCMeta):
    
    @abstractmethod
    def saveState(self):
        pass
    
    @abstractmethod
    def restoreState(self):
        pass

    @abstractmethod
    def restoreStateUntil(self, level):
        pass

    @abstractmethod
    def onRestore(self, listener):
        pass
    
    @abstractmethod
    def getLevel(self):
        pass

    @abstractmethod
    def makeStateRef(self, initValue):
        pass

    @abstractmethod
    def makeStateInt(self, initValue):
        pass
    
    @abstractmethod
    def makeStateMap(self):
        pass

    @abstractmethod
    def withNewState(self, body):
        pass