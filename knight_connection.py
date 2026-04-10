#!/usr/bin/env python3

def reduce(tup):
    x, y = tup[0], tup[1]
    x1, y1 = x - 1, y - 2
    x1, y1 = sorted([abs(x1), abs(y1)])
    x2, y2 = x - 2, y - 1
    x2, y2 = sorted([abs(x2), abs(y2)])
    return (x1, y1), (x2, y2)
    
def count(tup, cache):
    if tup in cache:
        return cache[tup]
    else:
        t1, t2 = reduce(tup)
        n = 1 + min(count(t1, cache), count(t2, cache))
        cache[tup] = n
        return n

def knightConnection(A, B):
    x, y = abs(A[0]-B[0]), abs(A[1]-B[1])
    x, y = sorted([x,y])
    cache = {(0,0): 0, (0,1): 3, (1,1): 2, (1,2): 1, (2,2): 4}
    n = count((x,y), cache)
    return n//2 + n%2
