#!/usr/bin/env python3

def is_square(x1, y1, x2, y2, point_set):
    # First Point
    xt1, yt1 = y1 - y2 + x1, x2 - x1 + y1
    if (xt1, yt1) not in point_set:
        return False
    xt2, yt2 = x2 - y2 + y1, y2 + x2 - x1
    if (xt2, yt2) in point_set:
        return [(xt1,yt1), (xt2,yt2)]

def countSquares(points):
    point_set = [(x,y) for x, y in points]
    sq_set = set()
    for p1 in range(len(points) - 1):
        for p2 in range(p1 + 1, len(points)):
            x1, y1 = points[p1]
            x2, y2 = points[p2]
            sq_points = is_square(x1, y1, x2, y2, point_set)
            if sq_points:
                sq_points += [(x1,y1),(x2,y2)]
                sq_points.sort()
                sq_set.add(tuple(sq_points))
                
    return len(sq_set)
