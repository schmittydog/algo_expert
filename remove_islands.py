#!/usr/bin/env python3

def removeIslands(matrix):
    height, width = len(matrix), len(matrix[0])
    visited = set()
    islands = set()
    for h in range(height):
        for w in range(width):
            if (h, w) in visited or matrix[h][w] == 0:
                continue
            remove = True
            land_mass = []
            dfs =[(h,w)]
            while dfs:
                h1, w1 = dfs.pop()
                if h1 == 0 or w1 == 0 or h1 == height - 1 or w1 == width - 1:
                    remove = False
                land_mass.append((h1,w1))
                visited.add((h1,w1))
                for move_h, move_w in [[0,1], [0,-1], [1,0],[-1,0]]:
                    nxt_h, nxt_w = h1 + move_h, w1 + move_w
                    if (nxt_h,nxt_w) in visited:
                        continue
                    if nxt_h < 0 or nxt_w < 0 or nxt_h >= height or nxt_w >= width:
                        continue
                    if matrix[nxt_h][nxt_w] == 0:
                        continue
                    visited.add((nxt_h,nxt_w))
                    dfs.append((nxt_h,nxt_w))
            if remove:
                print(land_mass)
                for isle in land_mass:
                    islands.add(isle)
    for h, w in islands:
        matrix[h][w] = 0
    return matrix
