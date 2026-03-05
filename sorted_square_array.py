#!/usr/bin/env python3

def sortedSquaredArray(array):
    '''
    Time: NLogN
    Space: N
    '''
    array.sort(key=abs)
    return [n**2 for n in array]

def sortedSquaredArray(array):
    '''
    Time: N
    Space: N
    '''
    l, r = 0, len(array) - 1
    squares = []
    while r >= l:
        if abs(array[r]) >= abs(array[l]):
            squares.append(array[r]**2)
            r -= 1
        else:
            squares.append(array[l]**2)
            l += 1
    squares.reverse()
    return squares
