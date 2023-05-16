#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The N-Queens problem.

<a href="https://www.csplib.org/Problems/prob054/">CSPLib</a>.

Authors: cutoutsy(cutoutsy@corp.netease.com)
Date: 2023/05/15

'''
import time
from minicp.cp.factory import *
from minicp.cp.branch_schema import *

def main():
    n = 12
    cp = makeSolver()
    q = []
    for _ in range(n):
        q.append(makeIntVar(cp, 0, n-1))
    for i in range(n):
        for j in range(i+1, n):
            cp.post(notEqual(q[i], q[j]))
            cp.post(notEqual(q[i], q[j], j - i))
            cp.post(notEqual(q[i], q[j], i - j))
    
    def f():
        idx = -1
        for k in range(len(q)):
            if q[k].size() > 1:
                idx = k
                break
        if idx == -1:
            return []
        else:
            qi = q[idx]
            v = qi.min()
            def left():
                qi.getSolver().post(equal(qi, v))
            def right():
                qi.getSolver().post(notEqual(qi, v))
            return [left, right]
    
    t0 = time.time()
    search = makeDfs(cp, f)
    stats = search.solve()
    t1 = time.time()
    print(stats)
    print("time (s): ", t1 - t0)


if __name__ == "__main__":
    main()