#!/usr/bin/env python3

# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        dfs = [self]
        while dfs:
            node = dfs.pop()
            array.append(node.name)
            dfs += reversed(node.children)
        return array
