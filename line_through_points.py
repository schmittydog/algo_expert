#!/usr/bin/python3

def get_mb(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x2 == x1:
        return ((float('inf'),x1))
    m = (y2-y1)/(x2-x1)
    b = y1-m*x1
    return (m,b)


def lineThroughPoints(points):
    if len(points) < 2:
        return 1
    d = {}
    for i in range(len(points)-1):
        for j in range(i+1, len(points)):
            t = get_mb(points[i], points[j])
            d[t] = d.get(t, set())
            d[t].add(tuple(points[i]))
            d[t].add(tuple(points[j]))
    return max(len(v) for v in d.values())
