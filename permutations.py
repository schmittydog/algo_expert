#!/usr/bin/env python3

def helper(remaining, candidate=[]):
    if not remaining:
        yield candidate
        return
    for i in range(len(remaining)):
        new_c = candidate + [remaining[i]]
        new_r = remaining[:i] + remaining[i+1:]
        yield from helper(new_r, new_c)
    
def getPermutations(array):
    if not array:
        return []
    return [perm for perm in helper(array)]
