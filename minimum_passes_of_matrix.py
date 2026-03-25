#!/usr/bin/env python3

from queue import deque

def minimumPassesOfMatrix(matrix):
    height, width = len(matrix), len(matrix[0])
    neg_set = set()
    visited = set()
    q = deque()
    for h in range(height):
        for w in range(width):
            if matrix[h][w] < 0:
                neg_set.add((h,w))
            elif matrix[h][w] == 0:
                visited.add((h,w))
            else:
                visited.add((h,w))
                q.append((0,h,w))
    passes = 0
    while q:
        passes, h, w = q.popleft()
        neg_set.discard((h,w))
        if not neg_set:
            break
        for dh, dw in [[1,0],[-1,0],[0,1],[0,-1]]:
            nxt_h, nxt_w = dh + h, dw + w
            if (nxt_h, nxt_w) in visited:
                continue
            if nxt_h < 0 or nxt_w < 0 or nxt_h >= height or nxt_w >= width:
                continue
            visited.add((nxt_h, nxt_w))
            q.append((passes+1, nxt_h, nxt_w))
    if neg_set:
        return -1
    return passes
        
