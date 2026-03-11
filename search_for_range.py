#!/usr/bin/env python3

def bin_search_right(array, target):
    left, right = 0, len(array) - 1
    while right >= left:
        mid = (right+left)//2
        if array[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return right if array[right] == target else -1
    
def bin_search_left(array, target):
    left, right = 0, len(array) - 1
    while right >= left:
        mid = (right+left)//2
        if array[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return left if array[left] == target else -1

def searchForRange(array, target):
    return [bin_search_left(array, target), bin_search_right(array, target)]
