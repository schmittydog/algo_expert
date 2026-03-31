#!/usr/bin/env python3

def swap_down(array):
    if len(array) == 1:
        return array
    val = array.pop()
    if val < array[-1]:
        val, array[-1] = array[-1], val
    swap_down(array)
    array.append(val)
    return array
    
def sortStack(stack):
    for i in range(len(stack) - 1):
        swap_down(stack)
    return stack
