#!/usr/bin/env python3

def firstNonRepeatingCharacter(string):
    '''
        Time: N
        Space: N
    '''
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    for i, char in enumerate(string):
        if char_count[char] == 1:
            return i
    return -1
