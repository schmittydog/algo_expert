#!/usr/bin/env python3

def balancedBrackets(string):
    stack = []
    map = {'(': ')', '{': '}', '[': ']'}
    for char in string:
        if char not in '{}()[]':
            continue
        if stack and map.get(stack[-1], 'Z') == char:
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0
