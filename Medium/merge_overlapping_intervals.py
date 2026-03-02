#!/usr/bin/env python3

def mergeOverlappingIntervals(intervals):
    '''
        Time: NLogN
        Space: N
    '''
    intervals.sort()
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            if interval[1] > merged[-1][1]:
                merged[-1][1] = interval[1]
    return merged
