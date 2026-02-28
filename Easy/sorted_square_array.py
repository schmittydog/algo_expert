#!/usr/bin/env python3

def sortedSquaredArray(array):
    '''
    Time: NLogN
    Space: N
    '''
    array.sort(key=abs)
    return [n**2 for n in array]


