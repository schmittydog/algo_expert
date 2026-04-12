#!/usr/bin/env python3

def get_islands(matrix):
    height, width = len(matrix), len(matrix[0])
    zeroes = set((h,w) for h in range(height) for w in range(width) if matrix[h][w] == 0)
    island_sets = []
    while zeroes:
        island = set()
        dfs = [zeroes.pop()]
        while dfs:
            h, w = dfs.pop()
            island.add((h,w))
            for dh, dw in [(0,1), (0,-1), (1,0), (-1,0)]:
                if (h+dh, w+dw) in zeroes:
                    dfs.append((h+dh, w+dw))
                    zeroes.remove((h+dh, w+dw))
        island_sets.append(island)
    return island_sets

def largestIsland(matrix):
    height, width = len(matrix), len(matrix[0])
    islands = get_islands(matrix)
    island_sizes = [len(island) for island in islands]
    for i, island in enumerate(islands):
        num = i+2
        for h, w in island:
            matrix[h][w] = num
    max_island = 0
    for h in range(height):
        for w in range(width):
            if matrix[h][w] == 1:
                island_set = set()
                for dh, dw in [(1,0), (-1,0), (0,1), (0,-1)]:
                    newh, neww = h + dh, w + dw
                    if newh < 0 or neww < 0 or newh >= height or neww >= width:
                        continue
                    if matrix[newh][neww] > 1:
                        island_set.add(matrix[newh][neww])
                cand = 1 + sum(island_sizes[i-2] for i in island_set)
                max_island = max(max_island, cand)
    return max_island
