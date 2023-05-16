#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/18

'''
import traceback
from minicp.engine.core.solver import Solver
from minicp.exception import InconsistencyError

class MiniCP(Solver):

    def __init__(self, sm):
        super().__init__()
        self.sm = sm
        self.propagationQueue = []
        self.fixPointListeners = []
    
    def getStateManager(self):
        return self.sm

    def schedule(self, c):
        if c.isActive() and not c.isScheduled():
            c.setScheduled(True)
            self.propagationQueue.append(c)

    def onFixPoint(listener):
        return super().onFixPoint()

    def fixPoint(self):
        try:
            while len(self.propagationQueue) > 0:
                self.propagate(self.propagationQueue.pop())
        except InconsistencyError as e:
            # print("minicp fixpoint exception...")
            while len(self.propagationQueue) > 0:
                self.propagationQueue.pop().setScheduled(False)
            # print(traceback.format_exc())
            raise e

    def propagate(self, c):
        c.setScheduled(False)
        if c.isActive():
            c.propagate()

    def post(self, c, enforceFixPoint=True):
        c.post()
        if enforceFixPoint:
            self.fixPoint()
    
    def minimize(self, x):
        return super().minimize()
    
