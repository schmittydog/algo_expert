#!/usr/bin/env python3

from heapq import heappop, heappush
def mergeSortedArrays(arrays):
    h = []
    for array in arrays:
        array.reverse()
        heappush(h, (array[-1], array))
    sorted_array = []
    while h:
        v, arr = heappop(h)
        sorted_array.append(v)
        arr.pop()
        if arr:
            heappush(h, (arr[-1], arr))
    return sorted_array
