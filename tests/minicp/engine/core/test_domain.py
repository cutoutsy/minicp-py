#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/05/04

'''
from minicp.cp.factory import *
from minicp.engine.core.sparse_set_domain import SparseSetDomain

class MyDomainListener:
    def __init__(self):
        self.nFix = 0
        self.nChange = 0
        self.nRemoveBelow = 0
        self.nRemoveAbove = 0
    
    def empty(self):
        pass
    
    def fix(self):
        self.nFix += 1
    
    def change(self):
        self.nChange += 1
    
    def changeMin(self):
        self.nRemoveBelow += 1
    
    def changeMax(self):
        self.nRemoveAbove += 1

class TestDomain:

    def testDomain1(self):
        cp = makeSolver()
        dlistener = MyDomainListener()
        dom = SparseSetDomain(cp.getStateManager(), 5, 10)
        
        dom.removeAbove(8, dlistener)

        assert 1 == dlistener.nChange
        assert 0 == dlistener.nFix
        assert 1 == dlistener.nRemoveAbove
        assert 0 == dlistener.nRemoveBelow

        dom.remove(6, dlistener)

        assert 2 == dlistener.nChange
        assert 0 == dlistener.nFix
        assert 1 == dlistener.nRemoveAbove
        assert 0 == dlistener.nRemoveBelow

        dom.remove(5, dlistener)

        assert 3 == dlistener.nChange
        assert 0 == dlistener.nFix
        assert 1 == dlistener.nRemoveAbove
        assert 1 == dlistener.nRemoveBelow

        dom.remove(7, dlistener)

        assert 4 == dlistener.nChange
        assert 1 == dlistener.nFix
        assert 1 == dlistener.nRemoveAbove
        assert 2 == dlistener.nRemoveBelow
    

    def testDomain2(self):
        cp = makeSolver()
        dom = SparseSetDomain(cp.getStateManager(), 5, 10)
        dlistener = MyDomainListener()

        dom.removeAllBut(7, dlistener)

        assert 1 == dlistener.nChange
        assert 1 == dlistener.nFix
        assert 1 == dlistener.nRemoveAbove
        assert 1 == dlistener.nRemoveBelow

    def testDomain3(self):
        cp = makeSolver()
        dom = SparseSetDomain(cp.getStateManager(), 5, 10)
        dlistener = MyDomainListener()

        dom.removeAbove(5, dlistener)

        assert 1 == dlistener.nChange
        assert 1 == dlistener.nFix
        assert 1 == dlistener.nRemoveAbove
        assert 0 == dlistener.nRemoveBelow