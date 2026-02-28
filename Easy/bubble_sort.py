#!/usr/bin/env python3

def bubbleSort(array):
    '''
        Time: N**2
        Space: 1
    '''
    for _ in range(len(array)):
        for i in range(1, len(array)):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
    return array

def bubbleSort(array):
    '''
        Time: N**2
        Space: 1
        With early return
    '''
    for _ in range(len(array)):
        no_swaps = True
        for i in range(1, len(array)):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
                no_swaps = False
        if no_swaps:
            return array
    return array
