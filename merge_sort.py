#!/usr/bin/env python3

def merge_arrays(a, b):
    ret_arr = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            ret_arr.append(a[i])
            i += 1
        else:
            ret_arr.append(b[j])
            j += 1
    ret_arr.extend(a[i:])
    ret_arr.extend(b[j:])
    return ret_arr

def mergeSort(array, l=0, r=None):
    if r is None:
        r = len(array) - 1
    if l == r:
        return [array[l]]
    if r - l == 1:
        a, b = array[l], array[r]
        return [a,b] if a < b else [b,a]
    mid = (r-l)//2
    left = mergeSort(array, l, l + mid)
    right = mergeSort(array, l + mid + 1, r)
    return merge_arrays(left, right)

