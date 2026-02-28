#!/usr/bin/env python3

def getNthFib(n):
    '''
        Time: N
        Space: 1
    '''
    x, y = 0, 1
    if n == 1 or n == 2:
        return n - 1
    for _ in range(n-2):
        x, y = y, x + y
    return y
