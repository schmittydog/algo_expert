#!/usr/bin/env python3

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root, count=0):
    '''
        Time: N
        Space: LogN
        Recursive traversal
    '''
    branch_sums = []
    if not root.left and not root.right:
        branch_sums.append(count+root.value)
        return branch_sums
    if root.left:
        branch_sums += branchSums(root.left, count+root.value)
    if root.right:
        branch_sums += branchSums(root.right, count+root.value)
    return branch_sums
