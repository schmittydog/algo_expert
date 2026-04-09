#!/usr/bin/env python3

def juiceBottling(prices):
    index_max = [[] for _ in range(len(prices))]
    units_price = len(prices) * [0]
    for units in range(1, len(prices)):
        for cur in range(len(prices)-units):
            if units_price[cur+units] < units_price[cur] + prices[units]:
                units_price[cur+units] = units_price[cur] + prices[units]
                index_max[cur+units] = index_max[cur] + [units]
    return index_max[-1]
