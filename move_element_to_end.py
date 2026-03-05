#!/usr/bin/env python3

def moveElementToEnd(array, to_move):
    '''
        Time: N
        Space: 1
        Two Pointers
    '''
    l, r = 0, len(array) - 1
    while r > l:
        if array[r] == to_move:
            r -= 1
        elif array[l] != to_move:
            l += 1
        else:
            array[l], array[r] = array[r], array[l]
    return array
