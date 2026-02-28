#!/usr/bin/env python3

def two_number_sum(array, target_sum):
    '''
        O(N) Time
        O(N) Space
    '''
    numbers_visited = set()
    for number in array:
        if target_sum - number in numbers_visited:
            target_numbers = [target_sum - number, number]
        numbers_visited.add(number)
    return []

def twoNumberSum(array, target_sum):
    ''' 
        O(Nlog(N)) Time
        O(1) Space
    '''
    array.sort()
    l, r = 0, len(array) - 1
    while l < r:
        s = array[l] + array[r]
        if s == target_sum:
            return [array[l], array[r]]
        elif s < target_sum:
            l += 1
        else:
            r -= 1
    return []

def twoNumberSum(array, target_sum):
    ''' 
        O(N**2) Time
        O(1) Space
    '''
    l = len(array)
    for i in range(l-1):
        for j in range(i+1, l):
            if array[i] + array[j] == target_sum:
                return [array[i], array[j]]
    return []
