#!/usr/bin/env python3

def largestRange(array):
    '''
        Time: NLogN
        Space: N
    '''
    arr = sorted(array)
    i, j = 0, 1
    range = [arr[0], arr[0]]
    while j < len(arr):
        start = arr[i]
        end = arr[i]
        while j < len(arr) and (arr[j] == arr[j-1] + 1 or arr[j] == arr[j-1]):
            end = arr[j]
            j += 1
        if end - start > range[1] - range[0]:
            range = [start, end]
        i, j = j, j + 1
    return range


def largestRange(array):
    '''
        Time: N
        Space: N
    '''
    s = set(array)
    longest = [array[0], array[0]]
    for n in array:
        if n not in s:
            continue
        start, end = n, n
        while end + 1 in s:
            end += 1
            s.remove(end)
        while start - 1 in s:
             start -= 1
             s.remove(start)
        if end - start > longest[1] - longest[0]:
            longest = [start, end]
    return longest
