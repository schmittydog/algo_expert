#!/usr/bin/env python3
'''
    Time: n * len(denoms)
    Space: 1
'''

def numberOfWaysToMakeChange(n, denoms):
    cache = [1] + n * [0]
    for denom in denoms:
        for i in range(0, n-denom+1):
            if cache[i]:
                cache[i+denom] += cache[i]
    return cache[-1]
