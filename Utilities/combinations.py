#!/usr/bin/env python3

def combinations(array, picks, start=0, combo=[]):
    for i in range(start, len(array)-picks):
        yield from combinations(a
