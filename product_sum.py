#!/usr/bin/env python3

# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, depth=1):
    count = 0
    for item in array:
        if isinstance(item, list):
            count += productSum(item, depth+1)
        else:
            count += item
    return count * depth
