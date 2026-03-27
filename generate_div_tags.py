#!/usr/bin/env python3

def tag_generator(open, close, arr=[]):
    if open == 0 and close == 0:
        yield ''.join(arr)
        return
    if close > open:
        yield from tag_generator(open, close-1, arr + ['</div>'])
    if open:
        yield from tag_generator(open-1, close, arr + ['<div>'])
    
def generateDivTags(num):
    return [str for str in tag_generator(num, num)]




for x in generateDivTags(3):
    print(x)
