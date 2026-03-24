#!/usr/bin/env python3

def quickselect(array, k, start=0, end=None):
    if end is None:
        end = len(array) - 1
    j = start
    for i in range(start+1, end+1):
        if array[i] < array[j]:
            array[i], array[j] = array[j], array[i]
            array[i], array[j+1] = array[j+1], array[i]
            j += 1
    if j == k - 1:
        return array[j]
    if j > k - 1:
        return quickselect(array, k, start, j-1)
    else:
        return quickselect(array, k, j+1, end)
