#!/usr/bin/env python3

from heapq import heappop, heappush

def laptopRentals(times):
    if not times:
        return 0
    times.sort()
    q = [times[0][1]]
    for idx in range(1, len(times)):
        start, end = times[idx]
        if start < q[0]:
            heappush(q, end)
        else:
            heappop(q)
            heappush(q, end)
    return len(q)
