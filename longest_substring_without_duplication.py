#!/usr/bin/env python3

def longestSubstringWithoutDuplication(string):
    ch_set = set()
    substring = [0,0]
    i, j = 0, 0
    while j < len(string):
        if string[j] not in ch_set:
            ch_set.add(string[j])
            if (j-i) > (substring[1] - substring[0]):
                substring = [i,j]
            j += 1
        else:
            while string[i] != string[j]:
                ch_set.remove(string[i])
                i += 1
            ch_set.remove(string[i])
            i += 1
    return string[substring[0]:substring[1]+1]
