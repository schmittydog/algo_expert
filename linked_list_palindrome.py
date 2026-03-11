#!/usr/bin/env python3

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListPalindrome(head):
    '''
        Time: N
        Space: N
    '''
    nums = []
    node = head
    while node:
        nums.append(node.value)
        node = node.next
    for i in range(len(nums)//2):
        if nums[i] != nums[len(nums)-1-i]:
            return False
    return True
