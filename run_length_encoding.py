#!/usr/bin/env python3

def encode(char, count):
    prefix, suffix = '', ''
    if count >= 9:
        prefix = count//9 * f'9{char}'
    if count%9 > 0:
        suffix = str(count%9) + char
    return prefix + suffix
        

def runLengthEncoding(string):
    '''
        Time: N
        Space: N
    '''
    current_char = string[0]
    count = 1
    encodes = []
    for i in range(1, len(string)):
        char = string[i]
        if char == current_char:
            count += 1
        else:
            encodes.append(encode(current_char, count))
            current_char = char
            count = 1
    encodes.append(encode(current_char, count))
    return ''.join(encodes)
    

