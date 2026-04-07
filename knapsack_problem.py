#!/usr/bin/env python3

def getPath(cache, items):
    depth, width = len(cache)-1, len(cache[0])-1
    path = []
    while width > 0 and depth > 0:
        cur_val = cache[depth][width]
        if cache[depth-1][width] < cur_val:
            path.append(depth-1)
            width -= items[depth-1][1]
        depth -= 1
    return path
        
def knapsackProblem(items, capacity):
    cache = [(capacity + 1) * [0]]
    for value, weight in items:
        next_row = (capacity + 1) * [0]
        for i in range(1, capacity+1):
            cur_max = max(cache[-1][i], next_row[i-1])
            if i >= weight:
                cur_max = max(cur_max, value + cache[-1][i-weight])
            next_row[i] = cur_max
        cache.append(next_row)
    max_value = cache[-1][-1]
    path = getPath(cache, items)
    return [max_value, path]
