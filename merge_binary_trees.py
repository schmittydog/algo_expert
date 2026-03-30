#!/usr/bin/env python3

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def mergeBinaryTrees(tree1, tree2):
    if tree1 is None and tree2 is None:
        return None
    tree = BinaryTree(0)
    if tree1:
        tree.value += tree1.value
    if tree2:
        tree.value += tree2.value
    if tree1 is None:
        tree.left = mergeBinaryTrees(None, tree2.left)
        tree.right = mergeBinaryTrees(None, tree2.right)
    elif tree2 is None:
        tree.left = mergeBinaryTrees(tree1.left, None)
        tree.right = mergeBinaryTrees(tree1.right, None)
    else:
        tree.left = mergeBinaryTrees(tree1.left, tree2.left)
        tree.right = mergeBinaryTrees(tree1.right, tree2.right)
    return tree
