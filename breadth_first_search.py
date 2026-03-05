#!/usr/bin/env python3

from queue import deque
# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        bfs = deque([self])
        while bfs:
            nxt = bfs.popleft()
            array.append(nxt.name)
            for child in nxt.children:
                bfs.append(child)
        return array
