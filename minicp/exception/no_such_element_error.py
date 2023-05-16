#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2023 NetEase.com, Inc. All Rights Reserved.
# Copyright 2023, The Fuxi AI Lab.
'''
desc

Authors: cutoutsy(cutoutsy@gmail.com)
Date: 2023/04/21

'''

class NoSuchElementError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.errorinfo = ErrorInfo
    
    def __str__(self) -> str:
        return self.errorinfo