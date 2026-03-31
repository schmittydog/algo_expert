#!/usr/bin/env python3

def minNumberOfJumps(array):
    if len(array) < 2:
        return 0
    idx = 0
    forward = array[0]
    jumps = 1
    while forward < len(array) - 1:
        for i in range(idx, forward + 1):
            forward = max(forward, i + array[i])
        jumps += 1
    return jumps
            
            
        
        

