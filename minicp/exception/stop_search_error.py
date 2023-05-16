#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Exception that is thrown to stop the execution of DFSearch.solve()

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/27

'''

class StopSearchError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.errorinfo = ErrorInfo
    
    def __str__(self) -> str:
        return self.errorinfo