#!/usr/bin/env python3

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(node):
    '''
        Time: N
        Space: 1
    '''
    head = node
    while node is not None and node.next is not None:
        if node.value == node.next.value:
            node.next = node.next.next
            continue
        node = node.next
    return head
