#!/usr/bin/python3

def apartmentHunting(blocks, reqs):
    current_proximity = len(reqs) * [None]
    proximity_tracker = [len(reqs) * [None] for _ in blocks]
    for b in range(len(blocks)):
        for r in range(len(reqs)):
            if blocks[b][reqs[r]]:
                current_proximity[r] = 0
            else:
                if current_proximity[r] is not None:
                    current_proximity[r] += 1
        proximity_tracker[b] = current_proximity.copy()
    current_proximity = len(reqs) * [None]
    for b in range(len(blocks)-1, -1, -1):
        for r in range(len(reqs)):
            if blocks[b][reqs[r]]:
                current_proximity[r] = 0
            else:
                if current_proximity[r] is not None:
                    current_proximity[r] += 1
            if proximity_tracker[b][r] is None:
                proximity_tracker[b][r] = current_proximity[r]
            else:
                if current_proximity[r]:
                    proximity_tracker[b][r] = min(proximity_tracker[b][r], current_proximity[r])
    min_sum = float('inf')
    min_index = 0
    print(proximity_tracker)
    for i in range(len(proximity_tracker)):
        psum = max(proximity_tracker[i])
        if psum < min_sum:
            min_sum = psum
            min_index = i
    return min_index
