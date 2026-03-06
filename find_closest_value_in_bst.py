#!/usr/bin/env python3

def findClosestValueInBst(tree, target, candidate=None):
    if tree is None:
        return candidate
    if candidate is None:
        candidate = tree.value
    if abs(tree.value-target) < abs(candidate-target):
        new_candidate = tree.value
    else:
        new_candidate = candidate
    if target < tree.value:
        return findClosestValueInBst(tree.left, target, new_candidate)
    else:
        return findClosestValueInBst(tree.right, target, new_candidate)

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

