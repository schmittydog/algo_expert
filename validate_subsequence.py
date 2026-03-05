#!/usr/bin/env python3

def isValidSubsequence(array, sequence):
    '''
        Time: N
        Space: 1
    '''
    sequence_index = 0
    for n in array:
        if n == sequence[sequence_index]:
            sequence_index += 1
        if sequence_index == len(sequence):
            return True
    return False
