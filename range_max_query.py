#!/usr/bin/env python3
from random import shuffle

class BinaryTree:
    def __init__(self, array, li=None, ri=None):
        self.li = 0 if li is None else li
        self.ri = len(array) - 1 if ri is None else ri
        self.max = None
        self.left_node = None
        self.right_node = None
        self.build(array)

    def build(self, array):
        if len(array) == 1:
            self.max = array[0]
            return
        left_array = array[:(self.ri-self.li+1)//2]
        right_array = array[(self.ri-self.li+1)//2:]
        self.left_node = BinaryTree(left_array, self.li, self.li + len(left_array) - 1)
        self.right_node = BinaryTree(right_array, self.li + len(left_array), self.ri)

    def populate_max(self):
        if self.max is None:
            self.left_node.populate_max()
            self.right_node.populate_max()
            self.max = max(self.left_node.max, self.right_node.max)
        return self.max

    def range_max(self, low, high):
        if low == self.li and high == self.ri:
            return self.max
        mid = self.li + (self.ri-self.li+1)//2 - 1
        rmax = float('-inf')
        if low <= mid:
            rmax = max(rmax, self.left_node.range_max(low, min(high, mid)))
        if high >= mid + 1:
            rmax = max(rmax, self.right_node.range_max(max(mid+1, low), high))
        return rmax

def get_range_max(array):
    rmax = BinaryTree(array)
    rmax.populate_max()
    return rmax

a = list(range(20))
shuffle(a)
rmax = get_range_max(a)

import sys
l, h = int(sys.argv[1]), int(sys.argv[2])
m = rmax.range_max(l, h)
print(a)
print(f'{m} at index {a.index(m)}')
