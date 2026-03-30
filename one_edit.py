#!/usr/bin/env python3

def oneEdit(one, two):
    l1, l2 = len(one), len(two)
    if abs(l2-l1) > 1:
        return False
    if l1 == l2:
        diffs = 0
        for i in range(l1):
            if one[i] != two[i]:
                diffs += 1
        return diffs <= 1
    if l1 > l2:
        l1, l2, one, two = l2, l1, two, one
    idx = 0
    for i in range(l2):
        if idx < l1 and one[idx] == two[i]:
            idx += 1
    return idx == len(one)
