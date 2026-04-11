#!/usr/bin/env python3

def waterArea(heights):
    left_max = 0
    water = 0
    water_to_add = 0
    for i in range(len(heights)):
        if heights[i] >= left_max:
            water += water_to_add
            water_to_add = 0
            left_max = heights[i]
        else:
            water_to_add += left_max - heights[i]
    right_max = 0
    water_to_add = 0
    for i in range(len(heights) -1, -1, -1):
        if heights[i] >= right_max:
            water += water_to_add
            water_to_add = 0
            right_max = heights[i]
        else:
            water_to_add += right_max - heights[i]
        if heights[i] == left_max:
            break
    return water
