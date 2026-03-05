#!/usr/bin/env python3

def generateDocument(characters, document):
    '''
        Time: N
        Space: N
    '''
    doc_map = {}
    for char in document:
        doc_map[char] = doc_map.get(char, 0) + 1
    for char in characters:
        if char in doc_map:
            doc_map[char] -= 1
            if doc_map[char] == 0:
                del(doc_map[char])
    return len(doc_map) == 0

