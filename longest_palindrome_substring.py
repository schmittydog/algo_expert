#!/usr/bin/env python3

def longestPalindromicSubstring(string):
    longest = string[0]
    for i in range(len(string)-1):
        for j in range(i+1, len(string)):
            if j-i+1 > len(longest):
                word = string[i:j+1]
                if word == word[::-1]:
                    longest = word
    return longest

# N^2
def longestPalindromicSubstring(string):
    longest = ''
    for idx in range(len(string)):
        # check even
        left, right = idx, idx-1
        while left > 0 and right < len(string) - 1 and string[left-1] == string[right+1]:
            left, right = left - 1, right + 1
        if right - left + 1 > len(longest):
            longest = string[left:right+1]
        # Check odd
        left, right = idx, idx
        while left > 0 and right < len(string) - 1 and string[left-1] == string[right+1]:
            left, right = left - 1, right + 1
        if right - left + 1 > len(longest):
            longest = string[left:right+1]
    return longest

