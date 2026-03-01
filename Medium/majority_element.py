#!/usr/bin/env python3

def majorityElement(array):
    '''
        Time: N
        Space: 1
    '''
    major = array[0]
    count = 1
    for i in range(1, len(array)):
        if array[i] == major:
            count += 1
        else:
            count -= 1
            if count == 0:
                major = array[i]
                count = 1
    return major
