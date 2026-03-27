#!/usr/bin/env python3

def radixSort(array):
    if not array:
        return array
    maxNumber = max(array)
    digits = len(str(maxNumber))
    div_by = 1
    for _ in range(digits):
        counts = 10 * [0]
        nxt_array = len(array) * [0]
        for n in array:
            counts[(n//div_by)%10] += 1
        for i in range(1, 10):
            counts[i] += counts[i-1]
        for n in reversed(array):
            digit = (n//div_by)%10
            counts[digit] -= 1
            nxt_array[counts[digit]] = n
        array = nxt_array
        div_by *= 10
    return array
