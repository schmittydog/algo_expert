#!/usr/bin/env python3

def tup_add(t1, t2):
    l = list(t1) + list(t2)
    s = set(l)
    if len(s) == 4:
        return tuple(sorted(s))
    
def fourNumberSum(array, targetSum):
    two_sums = {}
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            a, b = array[i], array[j]
            two_sums[a+b] = two_sums.get(a+b, [])
            two_sums[a+b].append((a,b))
    tup_set = set()
    for key, tup1s in two_sums.items():
        for tup2 in two_sums.get(targetSum-key, []):
            for tup1 in tup1s:
                quad = tup_add(tup1,tup2)
                if quad:
                    tup_set.add(quad)
    return [list(s) for s in tup_set]
