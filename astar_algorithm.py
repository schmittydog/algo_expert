#!/usr/bin/env python3

from heapq import heappush, heappop

class Path:
    def __init__(self, start, end, grid):
        self.path = [start]
        self.end = end
        self.height = len(grid)
        self.width = len(grid[0])
        
    def manhattan_distance(self):
        md = abs(self.path[-1][0] - self.end[0])
        md += abs(self.path[-1][1] - self.end[1])
        return md

    def finished(self):
        return self.path[-1] == self.end
        
    def total_distance(self):
        return len(self.path) + self.manhattan_distance()

    def __lt__(self, obj):
        return self.total_distance() < obj.total_distance()

    def new_path(self, coords, grid):
        new_path = Path([0,0], self.end, grid)
        new_path.path = self.path.copy()
        new_path.path += [coords]
        return new_path

    def get_next(self, grid):
        h_cur, w_cur = self.path[-1]
        for h, w in [[1,0], [-1,0], [0,1], [0,-1]]:
            h_next, w_next = h_cur+h, w_cur+w
            if h_next < 0 or h_next >= self.height or w_next < 0 or w_next >= self.width:
                continue
            if grid[h_next][w_next] == 1:
                continue
            yield self.new_path([h_next, w_next], grid)
            
def aStarAlgorithm(startRow, startCol, endRow, endCol, grid):
    height, width = len(grid), len(grid[0])
    start = [startRow,startCol]
    end = [endRow,endCol]
    visited = set(tuple(start))
    path = Path(start, end, grid)
    q = [path]
    while q:
        p = heappop(q)
        if p.finished():
            return p.path
        for next_p in p.get_next(grid):
            if tuple(next_p.path[-1]) in visited:
                continue
            visited.add(tuple(next_p.path[-1]))
            heappush(q,next_p)

    return []
