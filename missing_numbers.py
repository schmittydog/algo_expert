#!/usr/bin/env python3

def missingNumbers(nums):
    '''
        Time: N
        Space: N
    '''
    s = set(nums)
    print(s)
    return [n for n in range(1, len(nums+3)) if n not in s]

def missingNumbers(nums):
    '''
        Time: N
        Space: 1
    '''
    n = len(nums) + 2
    full_sum = (n*n+n)//2
    num_sum = sum(nums)
    diff = full_sum - num_sum
    sum_of_diffs = 0
    for n1 in range(diff-n, diff//2+1):
        sum_of_diffs += diff - 2*n1
    print(diff, sum_of_diffs)
    for num in nums:
        if num >= diff-n and num <= diff//2:
            sum_of_diffs += 2*n1 - diff
    n1 = (diff-sum_of_diffs)//2
    n2 = n1 + sum_of_diffs
    return sorted([n1,n2])

print(missingNumbers([1,3,4]))
