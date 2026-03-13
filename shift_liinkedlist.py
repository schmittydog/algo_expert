#!/usr/bin/env python3

# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    l = 0
    node = head
    while node:
        l += 1
        node = node.next
    cut = (l-k)%l
    if cut == 0:
        return head
    node = head
    for _ in range(cut-1):
        node = node.next
    new_head = node.next
    node.next = None
    n = new_head
    while n.next is not None:
        n = n.next
    n.next = head
    return new_head
