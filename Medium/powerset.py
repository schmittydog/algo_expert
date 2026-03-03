#!/usr/bin/env python3

def powerset(array):
    power_set = []
    for num in range(2**len(array)):
        candidate = []
        for i in range(len(array)):
            if num&2**i:
                candidate.append(array[i])
        power_set.append(candidate)
    return power_set
