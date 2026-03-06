#!/usr/bin/env python3

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(ll):
    slow = ll
    fast = ll
    while fast.next:
        slow = slow.next
        fast = fast.next
        if fast.next:
            fast = fast.next
    return slow
