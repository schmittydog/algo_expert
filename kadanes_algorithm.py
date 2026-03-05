#!/usr/bin/env python3

def kadanesAlgorithm(array):
    current_sum = 0
    current_max = -10**18
    for num in array:
        current_sum += num
        current_max = max(current_max, current_sum)
        if current_sum < 0:
            current_sum = 0
    return current_max
