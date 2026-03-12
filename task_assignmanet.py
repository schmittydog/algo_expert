#!/usr/bin/env python3

def taskAssignment(k, tasks):
    arr = [(n, i) for i, n in enumerate(tasks)]
    arr.sort()
    indices = []
    for i in range(k):
        indices.append([arr[i][1], arr[2*k-1-i][1]])
    return indices
