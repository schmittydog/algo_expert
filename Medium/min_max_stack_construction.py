#!/usr/bin/env python3

# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []
        
    def peek(self):
        if self.stack:
            return self.stack[-1][0]

    def pop(self):
        if self.stack:
            return self.stack.pop()[0]

    def push(self, number):
        if not self.stack:
            self.stack.append((number, number, number))
        else:
            nxt_min = min(number, self.stack[-1][1])
            nxt_max = max(number, self.stack[-1][2])
            self.stack.append((number, nxt_min, nxt_max))

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
            
    def getMax(self):
        if self.stack:
            return self.stack[-1][2]
