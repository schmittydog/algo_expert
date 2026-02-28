#!/usr/bin/env python3

def two_number_sum(array, target_sum):
    target_numbers = []
    numbers_visited = set()
    for number in array:
        if target_sum - number in numbers_visited:
            target_numbers = [target_sum - number, number]
            break
        numbers_visited.add(number)
    return target_numbers
