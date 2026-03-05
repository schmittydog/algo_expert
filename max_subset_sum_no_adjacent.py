#!/usr/bin/env python3

def maxSubsetSumNoAdjacent(array):
    '''
        Time: N
        Space: N
        Dynamic Programming
    '''
    if not array:
        return 0
    dp = [0] + array
    dp[1] = max((0, array[0]))
    max_sum = dp[1]
    for i in range(2, len(dp)):
        dp[i] = max((dp[i-2], dp[i-1], dp[i-2]+dp[i]))
        max_sum = max(max_sum, dp[i])
    return max_sum
    
def maxSubsetSumNoAdjacent(array):
    '''
        Time: N
        Space: 1
    '''
    if not array:
        return 0
    x, y = 0, 0
    for num in array:
        n = max(x, y, x+num)
        x, y = y, n
    return y
