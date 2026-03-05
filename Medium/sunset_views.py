#!/usr/bin/env python3

def sunsetViews(buildings, direction):
    start, end, inc = 0, len(buildings), 1
    if direction == 'EAST':
        start, end, inc = len(buildings)-1, -1, -1
    height = 0
    indices = []
    for i in range(start, end, inc):
        if buildings[i] > height:
            height = buildings[i]
            indices.append(i)
    if indices and indices[0] > indices[-1]:
        indices.reverse()
    return indices
