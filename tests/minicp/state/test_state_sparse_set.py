#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/05/04

'''
import pytest
from minicp.engine.core.minicp import MiniCP
from minicp.state.copier import Copier
from minicp.cp.factory import *
from minicp.cp.branch_schema import *
from minicp.state.copier import Copier
from minicp.state.state_sparse_set import StateSparseSet

class TestStateSparseSet:

    def testExample(self):
        sm = Copier()
        state_set = StateSparseSet(sm, 9, 0)
        sm.saveState()

        state_set.remove(4)
        state_set.remove(6)

        assert state_set.contains(4) == False
        assert state_set.contains(6) == False

        sm.restoreState()

        assert state_set.contains(4) == True
        assert state_set.contains(6) == True
    
    
    def testReversibleSparseSet(self):
        sm = Copier()
        state_set = StateSparseSet(sm, 10, 0)

        assert set(state_set.toArray()) == set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

        sm.saveState()

        state_set.remove(1)
        state_set.remove(0)

        assert 2 == state_set.min()

        state_set.remove(8)
        state_set.remove(9)

        assert set(state_set.toArray()) == set([2, 3, 4, 5, 6, 7])
        assert 7 == state_set.max()

        sm.restoreState()
        sm.saveState()
        
        assert 10 == state_set.size()

        for i in range(10):
            assert state_set.contains(i) == True
        
        assert state_set.contains(10) == False

        assert 0 == state_set.min()
        assert 9 == state_set.max()

        state_set.removeAllBut(2)

        for i in range(10):
            if i != 2:
                assert state_set.contains(i) == False
        
        assert state_set.contains(2) == True
        assert set(state_set.toArray()) == set([2])

        sm.restoreState()
        sm.saveState()

        assert 10 == state_set.size()
    
    def testRangeConstructor(self):
        sm = Copier()
        state_set = StateSparseSet(sm, 10, 0)

        for i in range(10):
            assert state_set.contains(i) == True

        sm.saveState()

        state_set.remove(4)
        state_set.remove(5)
        state_set.remove(0)
        state_set.remove(1)

        assert 2 == state_set.min()
        assert 9 == state_set.max()

        sm.saveState()

        state_set.removeAllBut(7)
        assert 7 == state_set.min()
        assert 7 == state_set.max()


        sm.restoreState()
        sm.restoreState()

        for i in range(10):
            assert state_set.contains(i) == True
    

    def testRemoveBelow(self):
        sm = Copier()
        state_set = StateSparseSet(sm, 10, 0)

        for i in range(10):
            assert state_set.contains(i) == True

        sm.saveState()

        state_set.removeBelow(5)

        assert 5 == state_set.min()
        assert 9 == state_set.max()

        sm.saveState()

        state_set.remove(7)
        state_set.removeBelow(7)

        assert 8 == state_set.min()

        sm.restoreState()
        sm.restoreState()

        for i in range(10):
            assert state_set.contains(i) == True
        

    def testRemoveAbove(self):
        sm = Copier()
        state_set = StateSparseSet(sm, 10, 0)

        for i in range(10):
            assert state_set.contains(i) == True

        sm.saveState()

        state_set.remove(1)
        state_set.remove(2)

        state_set.removeAbove(7)

        assert 0 == state_set.min()
        assert 7 == state_set.max()

        sm.saveState()

        state_set.removeAbove(2)

        assert 0 == state_set.max()

        sm.restoreState()
        sm.restoreState()

        for i in range(10):
            assert state_set.contains(i) == True