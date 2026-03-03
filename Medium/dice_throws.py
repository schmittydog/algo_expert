#!/usr/bin/env python3

def diceThrows(numDice, numSides, target):
    cache = [1] + target * [0]
    for num in range(1, numDice+1):
        cache_next = (target+1) * [0]
        for side in range(1, numSides+1):
            for i in range(target-side, -1, -1):
                cache_next[i+side] += cache[i]
        cache = cache_next
    return cache[-1]
