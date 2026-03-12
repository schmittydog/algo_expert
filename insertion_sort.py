#!/usr/bin/env python3

def insertionSort(array):
    for i in range(1, len(array)):
        while i >= 1 and array[i] < array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1
    return array
