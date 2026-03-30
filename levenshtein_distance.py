#!/usr/bin/env python3

def levenshteinDistance(str1, str2):
    short, long = (str2,str1) if len(str2) < len(str1) else (str1,str2)
    cache = list(range(len(short)+1))
    for i in range(len(long)):
        new_cache = [i+1] + (len(short)) * [0]
        for j in range(1, len(short) + 1):
            if short[j-1] == long[i]:
                new_cache[j] = cache[j-1]
            else:
                new_cache[j] = min(new_cache[j-1], cache[j], cache[j-1]) + 1
        cache = new_cache
    return cache[-1]
