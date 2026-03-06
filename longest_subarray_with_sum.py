#!/usr/bin/env python3

def longestSubarrayWithSum(array, target):
    longest = []
    current = array[0]
    left = 0
    right = 0
    while True:
        if current == target:
            if not longest or right - left > longest[1] - longest[0]:
                longest = [left, right]
        if current <= target or right == left:
            if right == len(array) - 1:
                break
            right += 1
            current += array[right]
        else:
            current -= array[left]
            left += 1
    return longest
