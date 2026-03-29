#!/usr/bin/env python3
from heapq import heappop, heappush

def laptopRentals(times):
    times.sort()
    q = []
    for start, end in times:
        if q and start >= q[0]:
            heappop(q)
        heappush(q, end)
    return len(q)
