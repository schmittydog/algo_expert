#!/usr/bin/env python3

def zeroSumSubarray(nums):
    '''
        Time: N
        Space: N
    '''
    sums = set([0])
    count = 0
    for num in nums:
        count += num
        if count in sums:
            return True
        sums.add(count)
    return False
