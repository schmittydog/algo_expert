#!/usr/bin/env python3

# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        self.heap = []
        for num in array:
            self.insert(num)
        return self.heap

    def siftDown(self):
        idx = 0
        while (idx + 1) <= len(self.heap)//2:
            idx1, idx2 = idx*2+1, idx*2+2
            if idx2 < len(self.heap):
                nxt_idx = idx1 if self.heap[idx1] <= self.heap[idx2] else idx2
            else:
                nxt_idx = idx1
            if self.heap[idx] > self.heap[nxt_idx]:
                self.heap[idx], self.heap[nxt_idx] = self.heap[nxt_idx], self.heap[idx]
                idx = nxt_idx
            else:
                break
            
    def siftUp(self):
        idx = len(self.heap) - 1
        while idx > 0:
            nxt_idx = idx//2 - 1 if idx%2 == 0 else idx//2
            if self.heap[idx] < self.heap[nxt_idx]:
                self.heap[idx], self.heap[nxt_idx] = self.heap[nxt_idx], self.heap[idx]
                idx = nxt_idx
            else:
                return

    def peek(self):
        if self.heap:
            return self.heap[0]

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        value = self.heap.pop()
        self.siftDown()
        return value

    def insert(self, value):
        self.heap.append(value)
        self.siftUp()

