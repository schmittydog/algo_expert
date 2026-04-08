#!/usr/bin/env python3

def bestDigits(number, numDigits):
    # Write your code here.
    if numDigits == 0:
        return number
    if len(number) == numDigits:
        return ''
    for i in range(1, len(number)):
        if number[i] > number[i-1]:
            return bestDigits(number[:i-1] + number[i:], numDigits-1)
    return number[:len(number)-numDigits]

def bestDigits(number, numDigits):
    stack = []
    for num in number:
        while numDigits and stack and num > stack[-1]:
            stack.pop()
            numDigits -= 1
        stack.append(num)
    return ''.join(stack[:len(number)-numDigits])

