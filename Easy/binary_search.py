#!/usr/bin/env python3

def binarySearch(array, target):
    '''
        Time: LogN
        Space: 1
    '''
    left, right = 0, len(array) - 1
    while right >= left:
        mid = (right + left)//2
        if array[mid] == target:
            return mid
        if array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
