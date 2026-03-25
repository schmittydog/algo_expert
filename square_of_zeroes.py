#!/usr/bin/env python3

def is_square(row, col, lt, rb):
    n = len(lt)
    size = lt[row][col]
    if size < 2:
        return False
    for i in range(1, size):
        r, c = row + i, col + i
        if r >= n or c >= n:
            break
        if rb[r][c] >= i:
            return True
    return False

def squareOfZeroes(matrix):
    n = len(matrix)
    lt = [n * [0] for _ in range(n)] # Left Top
    rb = [n * [0] for _ in range(n)] # Right Bottom
    for col in range(n):
        count = 0
        for row in range(n-1, -1, -1):
            count = 0 if matrix[row][col] == 1 else count + 1
            lt[row][col] = count
    for row in range(n):
        count = 0
        for col in range(n-1, -1, -1):
            count = 0 if matrix[row][col] == 1 else count + 1
            lt[row][col] = min(lt[row][col], count)
    for col in range(n):
        count = 0
        for row in range(n):
            count = 0 if matrix[row][col] == 1 else count + 1
            rb[row][col] = count
    for row in range(n):
        count = 0
        for col in range(n):
            count = 0 if matrix[row][col] == 1 else count + 1
            rb[row][col] = min(rb[row][col], count)
    return any(is_square(r, c, lt, rb) for r in range(n) for c in range(n))

