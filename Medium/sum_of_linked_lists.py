#!/usr/bin/env python3
'''
    Time: N
    Space: 1
'''

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def get_count(ll):
    mult = 1
    current = 0
    while ll is not None:
        current += mult * ll.value
        mult *= 10
        ll = ll.next
    return current

def sumOfLinkedLists(ll1, ll2):
    added = get_count(ll1) + get_count(ll2)
    head = LinkedList(added%10)
    added //= 10
    node = head
    while added:
        node.next = LinkedList(added%10)
        added //= 10
        node = node.next
    return head
