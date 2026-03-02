#!/usr/bin/env python3

def threeNumberSum(array, target_sum):
    '''
        Time: N**3
        Space: N
    '''
    threesums = []
    for i in range(len(array)-2):
        for j in range(i+1, len(array)-1):
            for k in range(j+1, len(array)):
                if array[i] + array[j] + array[k] == target_sum:
                    to_add = [array[i], array[j], array[k]]
                    to_add.sort()
                    threesums.append(to_add)
    threesums.sort()
    return threesums
