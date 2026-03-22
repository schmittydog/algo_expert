#!/usr/bin/env python3

from heapq import heappop, heappush

def dijkstrasAlgorithm(start, edges):
    costs = len(edges) * [-1]
    costs[start] = 0
    q = []
    for dest, cost in edges[start]:
        heappush(q, (cost, dest))
    visited = set([start])
    while q:
        print(q)
        cost, dest = heappop(q)
        if dest in visited:
            continue
        costs[dest] = cost
        visited.add(dest)
        for nxt_dest, nxt_cost in edges[dest]:
            if nxt_dest not in visited:
                heappush(q, (cost+nxt_cost, nxt_dest))
    return costs
