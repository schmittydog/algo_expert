#!/usr/bin/env python3

def partition(array, start, end):
    j = end
    for i in range(end, start-1, -1):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]
            array[i], array[j-1] = array[j-1], array[i]
            j -= 1
    if j-1 > start:
        partition(array, start, j-1)
    if j+1 < end:
        partition(array, j+1, end)
        
def quickSort(array):
    partition(array, 0, len(array)-1)
    return array
