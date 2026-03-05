#!/usr/bin/env python3

def bestSeat(seats):
    '''
        Time: N
        Space: 1
    '''
    right = 0
    max_zeros = 0
    cur_zeros = 0
    for i in range(len(seats)):
        if seats[i] == 1:
            cur_zeros = 0
        else:
            cur_zeros += 1
            if cur_zeros > max_zeros:
                max_zeros = cur_zeros
                right = i
    if right == 0:
        return -1
    return right - max_zeros + 1 + (max_zeros-1)//2
