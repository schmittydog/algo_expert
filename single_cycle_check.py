#!/usr/bin/env python3

def hasSingleCycle(array):
    visited = set()
    l = len(array)
    i = 0
    while i not in visited:
        visited.add(i)
        i = (array[i]+i)%l
    return len(visited) == len(array) and i == 0
