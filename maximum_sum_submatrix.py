#!/usr/bin/env python3
from copy import deepcopy

def get_max(mat, s):
    max_mat = -10**18
    for row in range(len(mat)-s+1):
        for col in range(len(mat[0])-s+1):
            mat_sum = mat[row+s-1][col+s-1]
            if row > 0:
                mat_sum -= mat[row-1][col+s-1]
            if col > 0:
                mat_sum -= mat[row+s-1][col-1]
            if row > 0 and col > 0:
                mat_sum += mat[row-1][col-1]
            max_mat = max(max_mat, mat_sum)
    return max_mat

def maximumSumSubmatrix(matrix, size):
    h, w = len(matrix), len(matrix[0])
    mat_sum = deepcopy(matrix)
    for row in range(h):
        for col in range(1, w):
            mat_sum[row][col] += mat_sum[row][col-1]
    for row in range(1,h):
        for col in range(w):
            mat_sum[row][col] += mat_sum[row-1][col]
    return get_max(mat_sum, size)
