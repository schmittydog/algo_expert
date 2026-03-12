#!/usr/bin/env python3

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_symmetrical(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    if t1.value != t2.value:
        return False
    return is_symmetrical(t1.left, t2.right) and is_symmetrical(t1.right, t2.left)

def symmetricalTree(tree):
    # Write your code here.
    return is_symmetrical(tree.left, tree.right)
