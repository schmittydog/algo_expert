#!/usr/bin/env python3

import heapq

def findThreeLargestNumbers(array):
    '''
        Time: NLog(3)
        Space: 1
    '''
    largest_heap = []
    heapq.heapify(largest_heap)
    for num in array:
        if len(largest_heap) < 3 or num > largest_heap[0]:
            heapq.heappush(largest_heap, num)
        if len(largest_heap) > 3:
            heapq.heappop(largest_heap)
    return sorted(largest_heap)

def findThreeLargestNumbers(array):
    '''
        Time: NLog(3)
        Space: 1
    '''
    largest = []
    for num in array:
        if len(largest) < 3 or largest[-1] < num:
            largest.append(num)
        largest.sort(reverse=True)
        if len(largest) > 3:
            largest.pop()
    largest.reverse()
    return largest
