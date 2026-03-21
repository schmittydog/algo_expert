#!/usr/bin/env python3

class Spiral:
    def __init__(self, array):
        self.array = array
        self.height = len(array)
        self.width = len(array[0])
        self.current = (0, 0)
        self.moves = [(0,1), (1,0), (0,-1), (-1,0)]
        self.move_idx = 0
        self.visited = set()

    def traverse(self):
        while self.current:
            h, w = self.current
            yield self.array[h][w]
            self.visited.add((h,w))
            self.move()

    def move(self):
        # Check next move
        h, w = self.current
        h_add, w_add = self.moves[self.move_idx]
        h_nxt, w_nxt = h + h_add, w + w_add
        # If valid, update new current
        if self.valid_coords((h_nxt, w_nxt)):
            self.current = (h_nxt, w_nxt)
        else:
            self.move_idx += 1
            self.move_idx %= 4
            h_add, w_add = self.moves[self.move_idx]
            h_nxt, w_nxt = h + h_add, w + w_add
            if self.valid_coords((h_nxt, w_nxt)):
                self.current = (h_nxt, w_nxt)
            else:
                self.current = None
        
    def valid_coords(self, coords):
        if coords in self.visited:
            return False
        if coords[0] < 0 or coords[0] >= self.height:
            return False
        if coords[1] < 0 or coords[1] >= self.width:
            return False
        return True

def spiralTraverse(array):
    spiral = Spiral(array)
    return [n for n in spiral.traverse()]
