#!/usr/bin/env python3

def next_row(arr):
    nxt_row = len(arr) * [0]
    for i in range(len(arr)):
        if i > 0 and arr[i]&1:
            nxt_row[i-1] |= 1
        if i < len(arr) - 1 and arr[i]&4:
            nxt_row[i+1] |= 4
        if arr[i]&2:
            nxt_row[i] |= 2
    return nxt_row

def solve(n, arr):
    if n == 0:
        return 1
    sum = 0
    for i, val in enumerate(arr):
        if val == 0:
            narr = arr.copy()
            narr[i] = 7
            nxt_row = next_row(narr)
            sum += solve(n-1, nxt_row)
    return sum

def nonAttackingQueens(n):
    return solve(n, n*[0])


print(nonAttackingQueens(12))
