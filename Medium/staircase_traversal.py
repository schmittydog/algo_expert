#!/usr/bin/env python3

def staircaseTraversal(height, maxSteps):
    '''
        Time: height * maxSteps
        Space: maxSteps
        Dynamic Programming
    '''
    dp = [1] + height * [0]
    for i in range(len(dp)):
        for j in range(1, maxSteps+1):
            if i + j >= len(dp):
                break
            dp[i+j] += dp[i]
    return dp[-1]
