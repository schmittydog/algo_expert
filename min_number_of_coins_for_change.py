#!/usr/bin/env python3

def minNumberOfCoinsForChange(n, denoms):
    dp = [0] + n*[float('inf')]
    for denom in denoms:
        for i in range(n+1-denom):
            dp[i+denom] = min(dp[i+denom], dp[i] + 1)
    if dp[-1] == float('inf'):
        return 
    return dp[-1]
