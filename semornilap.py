#!/usr/bin/env python3

def semordnilap(words):
    '''
        Time: N
        Space: N
    '''
    word_set = set()
    palindromes = set()
    for word in words:
        if word[::-1] in word_set:
            palindromes.add(word)
        else:
            word_set.add(word)
    return [[pali, pali[::-1]] for pali in palindromes]
