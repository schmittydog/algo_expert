#!/usr/bin/env python3

def smallestDifference(arr1, arr2):
    '''
        Time: NLogN
        Space: N
        Two Pointers
    '''
    a, b = sorted(arr1), sorted(arr2)
    ai, bi = 0, 0
    la, lb = len(a), len(b)
    sdiff = [arr1[0], arr2[0]]
    while ai < la and bi < lb:
        if abs(a[ai]-b[bi]) < abs(sdiff[0]-sdiff[1]):
            sdiff[0], sdiff[1] = a[ai], b[bi]
        if a[ai] <= b[bi]:
            if ai < la:
                ai += 1
        else:
            if bi < lb:
                bi += 1
    return sdiff

def smallestDifference(arr1, arr2):
    '''
        Time: N**2
        Space: 1
    '''
    smallest = [arr1[0], arr2[0]]
    for a in arr1:
        for b in arr2:
            if abs(a-b) < abs(smallest[0]-smallest[1]):
                smallest[0] = a
                smallest[1] = b
    return smallest
