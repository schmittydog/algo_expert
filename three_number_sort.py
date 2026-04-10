#!/usr/bin/env python3

def threeNumberSort(array, order):
    i, j = 0, len(array) - 1
    while j > i:
        while j > 0 and array[j] == order[-1]:
            j -= 1
        while i < len(array) and array[i] != order[-1]:
            i += 1
        if j > i:
            array[j], array[i] = array[i], array[j]
    i, j = 0, len(array) - 1
    while j > i:
        while j > 0 and array[j] != order[0]:
            j -= 1
        while i < len(array) and array[i] != order[1]:
            i += 1
        if j > i:
            array[j], array[i] = array[i], array[j]
    return array
