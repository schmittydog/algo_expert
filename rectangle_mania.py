#!/usr/bin/env python3

def rectangleMania(coords):
    count = 0
    coord_set = set(tuple(coord) for coord in coords)
    for i in range(len(coords)-1):
        for j in range(i+1, len(coords)):
            p1, p2 = coords[i], coords[j]
            x1, x2, y1, y2 = p1[0], p2[0], p1[1], p2[1]
            if (x1 < x2 and y1 < y2) or (x2 < x1 and y2 < y1):
                if (x1, y2) in coord_set and (x2, y1) in coord_set:
                    count += 1
    return count
