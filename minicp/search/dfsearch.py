#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/19

'''
import time
import traceback
from minicp.search.search_statistics import SearchStatistics
from minicp.engine.constraints.not_equal import NotEqual
from minicp.engine.constraints.equal import Equal
from minicp.engine.constraints.not_equal_num import NotEqualNum
from minicp.engine.constraints.equal_num import EqualNum
from minicp.state.copier import Copier
# from minicp.exception.in_consistency_error import InconsistencyError
from minicp.exception import *

class DFSearch:
    def __init__(self, sm: Copier, branching):
        """
        :param sm: the state manager that will be saved and restored 
                   at each node of the search tree
        """
        self.sm = sm
        self.branching = branching
        self.currNodeIdId = None
        self.onSolution_func = None
    
    def onSolution(self, f=None):
        self.onSolution_func = f

    def solve(self, limit=None):
        statistics = SearchStatistics()
        self.currNodeIdId = 0
        level = self.sm.withNewState()
        print("DFSearch solve level = ", level)
        try:
            self.dfs(statistics, limit, -1, -1)
            statistics.setCompleted()
        except StopSearchError as e:
            print("StopSearchError")
        except Exception as e:
            # raise InconsistencyError("InconsistencyError")
            print("dfs with explicit stack needed to pass this test")
            print(traceback.format_exc())
            raise e

        self.sm.restoreStateUntil(level)
        return statistics


    def dfs(self, statistics: SearchStatistics, limit, parentId, position):
        if limit is not None and limit(statistics):
            print("stop dfs")
            raise StopSearchError("StopSearchError")
        nodeId = self.currNodeIdId + 1
        
        branches = self.branching()
        if len(branches) == 0:
            print("branches is empty, solution found.")
            if self.onSolution_func is not None:
                self.onSolution_func()
            statistics.incrSolutions()
        else:
            pos = 0
            for b in branches:
                p = pos
                level = self.sm.withNewState()
                try:
                    statistics.incrNodes()
                    b()
                    self.dfs(statistics, limit, nodeId, p)
                except InconsistencyError as e:
                    print("dfs exception failures add.")
                    self.currNodeIdId += 1
                    statistics.incrFailures()
                self.sm.restoreStateUntil(level)

                pos += 1
                


