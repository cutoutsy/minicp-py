#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/19

'''

class SearchStatistics:
    
    def __init__(self):
        self.nFailures = 0
        self.nNodes = 0
        self.nSolutions = 0
        self.completed = False
    
    def incrFailures(self):
        self.nFailures += 1
    
    def incrNodes(self):
        self.nNodes += 1

    def incrSolutions(self):
        self.nSolutions += 1
    
    def setCompleted(self):
        self.completed = True

    def nFailures(self):
        return self.nFailures
    
    def nNodes(self):
        return self.nNodes
    
    def nSolutions(self):
        return self.nSolutions
    
    def completed(self):
        return self.completed

    def __str__(self):
        return "\n\t#choice: " + str(self.nNodes) \
                + "\n\t#fail: " + str(self.nFailures) \
                + "\n\t#sols : " + str(self.nSolutions) \
                + "\n\tcompleted : " + str(self.completed) + "\n"