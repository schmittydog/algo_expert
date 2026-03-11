#!/usr/bin/env python3

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(one, two):
    # we're added to one
    if two.value < one.value:
        one, two = two, one
    # keep head around
    orig = one # Track to send head
    while two:
        if one.next is None:
            one.next = two
            two = None
            break
        if two.value >= one.value and two.value <= one.next.value:
            tmp = two
            two = two.next
            tmp.next = one.next
            one.next = tmp
        one = one.next
    return orig
