#!/usr/bin/env python3

def longestPeak(array):
    longest_peak = 0
    for i in range(1, len(array) - 1):
        if array[i] > array[i-1] and array[i] > array[i+1]:
            start, end = i - 1, i + 1
            while start > 0 and array[start] > array[start-1]:
                start -= 1
            while end < len(array) - 1 and array[end] > array[end+1]:
                end += 1
            longest_peak = max(longest_peak, end - start + 1)
    return longest_peak
