#!/usr/bin/env python3

def minimumWaitingTime(queries):
    queries.sort()
    cur_sum = 0
    previous = 0
    last_previous = 0
    for query in queries:
        cur_sum += previous
        previous = query + last_previous
        last_previous = previous
    return cur_sum
