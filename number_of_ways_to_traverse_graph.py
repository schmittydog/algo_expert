#!/usr/bin/env python3

def numberOfWaysToTraverseGraph(width, height):
    legs = width + height - 2
    choices = height - 1
    paths = 1
    for i in range(choices):
        paths *= legs - i
        paths //= 1 + i
    return paths
