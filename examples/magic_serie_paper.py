#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The Magic Series problem.

<a href="https://www.csplib.org/Problems/prob019/">CSPLib</a>.

Authors: cutoutsy(cutoutsy@corp.netease.com)
Date: 2023/05/15

'''
import time
from minicp.cp.factory import *
from minicp.cp.branch_schema import *

def main():
    n = 10
    cp = makeSolver()
    s = []
    for _ in range(n):
        s.append(makeIntVar(cp, 0, n-1))
    
    for i in range(n):
        fi = i
        cp.post(sum_c(s[i], [isEqual(s[j], fi) for j in range(n)]))
    
    cp.post(sum_c(n, s))
    cp.post(sum_c(n, [mul(s[i], i) for i in range(n)]))
    
    def f():
        idx = -1
        for k in range(len(s)):
            if s[k].size() > 1:
                idx = k
                break
        if idx == -1:
            return []
        else:
            qi = s[idx]
            v = qi.min()
            def left():
                qi.getSolver().post(equal(qi, v))
            def right():
                qi.getSolver().post(notEqual(qi, v))
            return [left, right]
    def so():
        print("solution: ", [s_.min() for s_ in s])
    
    t0 = time.time()
    search = makeDfs(cp, f)
    search.onSolution(so)
    stats = search.solve()
    t1 = time.time()
    print(stats)
    print("time (s): ", t1 - t0)

if __name__ == "__main__":
    main()