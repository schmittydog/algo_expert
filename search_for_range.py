#!/usr/bin/env python3

def bin_search_right(array, target):
    if array[-1] == target:
        return len(array) - 1
    left, right = 0, len(array) - 1
    while right >= left:
        mid = (right+left)//2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] == target:
            if array[mid+1] != target:
                return mid
            else:
                left = mid + 1
        else:
            right = mid - 1
    return -1

def bin_search_left(array, target):
    if array[0] == target:
        return 0
    left, right = 0, len(array) - 1
    while right >= left:
        mid = (right+left)//2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] == target:
            if array[mid-1] != target:
                return mid
            else:
                right = mid
        else:
            right = mid - 1
    return -1

def searchForRange(array, target):
    return [bin_search_left(array, target), bin_search_right(array, target)]
