#!/usr/bin/env python3

def has_cycle(idx, edges, visited, count=1):
    if count > len(edges):
        return True
    if idx in visited:
        return False
    for nxt_idx in edges[idx]:
        if has_cycle(nxt_idx, edges, visited, count+1):
            return True
    visited.add(idx)
    return False
    
def cycleInGraph(edges):
    visited = set()
    for i in range(len(edges)):
        if has_cycle(i, edges, visited):
            return True
    return False
