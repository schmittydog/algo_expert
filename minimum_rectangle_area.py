#!/usr/bin/env python3

def square_area(p1, p2, point_set):
    # Check that it's a diagonal
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2 or y1 == y2:
        return
    p3, p4 = (x1, y2), (x2, y1)
    if p3 in point_set and p4 in point_set:
        return abs((x1-x2) * (y1-y2))
    
def minimumAreaRectangle(points):
    point_set = set(tuple(point) for point in points)
    min_area = 10**18
    for i in range(len(points) - 1):
        for j in range(i+1, len(points)):
            p1, p2 = points[i], points[j]
            area = square_area(p1, p2, point_set)
            if area:
                min_area = min(min_area, area)
    return min_area if min_area != 10**18 else 0
