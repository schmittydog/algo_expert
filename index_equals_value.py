#!/usr/bin/python3

def indexEqualsValue(array):
    l, r = 0, len(array) - 1
    while r > l:
        mid = (r + l)//2
        if mid > array[mid]:
            l = mid + 1
        else:
            r = mid
    return l if array and array[l] == l else -1
