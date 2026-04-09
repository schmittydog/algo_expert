#!/usr/bin/env python3

def minimumCharactersForWords(words):
    d = {}
    for word in words:
        w = {}
        for ch in word:
            w[ch] = w.get(ch, 0) + 1
        for ch, count in w.items():
            d[ch] = max(count, d.get(ch, 0))
    ret = []
    for ch, count in d.items():
        ret.extend(count*[ch])
    return ret
