#!/usr/bin/env python3

def selectionSort(array):
    '''
        Time: N**2
        Space: 1
    '''
    for i in range(len(array)):
        min_index = i
        min_value = array[i]
        for j in range(i+1, len(array)):
            if array[j] < min_value:
                min_index = j
                min_value = array[j]
        array[i], array[min_index] = array[min_index], array[i]
    return array
