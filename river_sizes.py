#!/usr/bin/env python3

def riverSizes(matrix):
    '''
        Time: HxW
        Space: HxW
    '''
    # height, width
    h, w = len(matrix), len(matrix[0])
    # visited set
    v = set()
    river_lengths = []
    for height in range(h):
        for width in range(w):
            if (height, width) in v:
                continue
            if matrix[height][width] == 0:
                continue
            bfs = [(height, width)]
            cur_river_len = 0
            while bfs:
                cur_cell = bfs.pop()
                v.add(cur_cell)
                cur_river_len += 1
                for move in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nxt_h, nxt_w = cur_cell[0]+move[0], cur_cell[1]+move[1]
                    if nxt_h >= h or nxt_h < 0 or nxt_w >= w or nxt_w < 0:
                        continue
                    if matrix[nxt_h][nxt_w] == 0:
                        continue
                    if (nxt_h, nxt_w) in v:
                        continue
                    bfs.append((nxt_h, nxt_w))
                    v.add((nxt_h, nxt_w))
            river_lengths.append(cur_river_len)
    river_lengths.sort()
    return river_lengths
