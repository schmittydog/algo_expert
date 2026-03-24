#!/usr/bin/env python3

class HeapSort:
    def __init__(self, array):
        self.array = array

    def sift_down(self, i):
        arr, l = self.array, len(self.array)
        if (2*i + 1) >= l:
            return
        if (2*i + 2) >= l:
            idx_swap = 2*i + 1
        else:
            idx_swap = 2*i+1 if arr[2*i+1] < arr[2*i+2] else 2*i+2
        if arr[idx_swap] < arr[i]:
            arr[idx_swap], arr[i] = arr[i], arr[idx_swap]
            self.sift_down(idx_swap)

    def build_heap(self):
        for i in range(len(self.array)-1, -1, -1):
            self.sift_down(i)

    def heap_sort(self):
        self.build_heap()
        heap_sorted = []
        for i in range(len(self.array)-1, -1, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            heap_sorted.append(self.array.pop())
            self.sift_down(0)
            print(self.array)
        return heap_sorted

def heapSort(array):
    h = HeapSort(array)
    return h.heap_sort()
