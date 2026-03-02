#!/usr/bin/env python3

def missingNumbers(nums):
    '''
        Time: N
        Space: N
    '''
    s = set(nums)
    print(s)
    return [n for n in range(1, len(nums+3)) if n not in s]


print(missingNumbers([1,3,4]))
