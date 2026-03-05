#!/usr/bin/env python3

def nonConstructibleChange(coins):
    '''
        Time: NLogN
        Space: 1
    '''
    coins.sort()
    min_value = 0
    for coin in coins:
        if coin > min_value + 1:
            break
        min_value += coin
    return min_value + 1
