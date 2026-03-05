#!/usr/bin/env python3

from heapq import heapify, heappop, heappush

# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.

class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None

    def insert(self, number):
        if self.median is None:
            self.left_heap = []
            self.right_heap = []
        left_heap, right_heap = self.left_heap, self.right_heap
        heappush(right_heap, number)
        heappush(left_heap, -heappop(right_heap))
        while len(left_heap) > len(right_heap) + 1:
            heappush(right_heap, -heappop(left_heap))
        if len(left_heap) > len(right_heap):
            self.median = -left_heap[0]
        else:
            self.median = (right_heap[0] - left_heap[0])/2
                       
    def getMedian(self):
        return self.median
