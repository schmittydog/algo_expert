#!/usr/bin/python3

def minHeightBst(array):
    if not array:
        return None
    split = len(array)//2 + len(array)%2
    left = array[:split]
    right = array[split:]
    node = BST(left.pop())
    node.left = minHeightBst(left)
    node.right = minHeightBst(right)
    return node

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
