#!/usr/bin/env python3

def sweetAndSavory(dishes, target):
    dishes.sort()
    d = [0,0]
    nearest = float('inf')
    i, j = 0, len(dishes) - 1
    while i < j and dishes[i] < 0 and dishes[j] > 0:
        tgt = dishes[i] + dishes[j]
        if tgt == target:
            return [dishes[i], dishes[j]]
        if tgt < target:
            if target - tgt < nearest:
                nearest = target - tgt
                d = [dishes[i], dishes[j]]
            i += 1
        else:
            j -= 1
    return d
