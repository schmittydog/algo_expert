#!/usr/bin/env python3

def nodeDepths(root, depth=0):
    '''
        Time: N
        Space: 1
        DFS
    '''
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def nodeDepths(root, depth=0):
    '''
        Time: N
        Space: N
        BFS
    '''
    count = 0
    queue = [(root, 0)]
    while queue:
        node, depth = queue.pop()
        if node is None:
            continue
        count += depth
        queue.append((node.left, depth + 1))
        queue.append((node.right, depth + 1))
    return count
