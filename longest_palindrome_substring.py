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
