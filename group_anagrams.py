#!/usr/bin/env python3

def groupAnagrams(words):
    '''
        Time: W*NLogN
        Space: N*W
    '''
    word_dict = {}
    for word in words:
        hash = ''.join(sorted(word))
        word_dict[hash] = word_dict.get(hash, []) + [word]
    return [value for value in word_dict.values()]
