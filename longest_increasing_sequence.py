#!/usr/bin/env python3
def bisect_left(arr, n):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (right + left) // 2
        if arr[mid][-1] >= n:
            right = mid 
        else:
            left = mid + 1
    return left

def longestIncreasingSubsequence(array):
    '''
        Time: nlogn
        Space: n
    '''
    cache = [[array[0]]]
    for i in range(1, len(array)):
        n = array[i]
        if n <= cache[0][-1]:
            cache[0][-1] = n
        elif n > cache[-1][-1]:
            cache.append(cache[-1] + [n])
        else:
            idx = bisect_left(cache, n)
            if n < cache[idx][-1]:
                cache[idx] = cache[idx-1] + [n]
    return cache[-1]
