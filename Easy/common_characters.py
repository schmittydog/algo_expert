#!/usr/bin/env python3

def commonCharacters(strings):
    '''
        Time: N
        Space: N
    '''
    string_set = set(strings[0])
    for i in range(1, len(strings)):
        new_string = set(strings[i])
        string_set &= new_string
    return list(string_set)
