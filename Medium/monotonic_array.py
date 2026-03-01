#!/usr/bin/env python3

def isMonotonic(array):
    '''
        Time: N
        Space: 1
    '''
    non_inc, non_dec = True, True
    for i in range(1, len(array)):
        if array[i] - array[i-1] < 0:
            non_dec = False
        if array[i] - array[i-1] > 0:
            non_inc = False
    return non_inc or non_dec
