#!/usr/bin/env python3

def zigzagTraverse(array):
    h, w = len(array), len(array[0])
    zigzag = []
    reverse = 1
    for i in range(h):
        zz = []
        r, c = i, 0
        while r >= 0 and r < h and c >= 0 and c < w:
            zz.append(array[r][c])
            r, c = r-1, c+1
        if reverse:
            zz.reverse()
        zigzag += zz
        reverse ^= 1
    for i in range(1, w):
        zz = []
        r, c = h-1, i
        while r >= 0 and r < h and c >= 0 and c < w:
            zz.append(array[r][c])
            r, c = r-1, c+1
        if reverse:
            zz.reverse()
        zigzag += zz
        reverse ^= 1
    return zigzag
