#!/usr/bin/env python3

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            str = string[i:]
            root = self.root
            for ch in str:
                if ch not in root:
                    root[ch] = {}
                root = root[ch]
            root["*"] = True

    def contains(self, string):
        root = self.root
        for ch in string:
            if ch not in root:
                return False
            root = root[ch]
        return '*' in root
