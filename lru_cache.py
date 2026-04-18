#!/usr/bin/env python3

# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class DLL:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __bool__(self):
        return self.length > 0

    def push(self, node):
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.length += 1

    def update(self, node):
        if node == self.head:
            return
        if node == self.tail:
            self.pop()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.push(node)
            
    def pop(self):
        if self.length <= 0:
            raise Exception('Popping from empty list')
        node = self.tail
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return node

class LRUCache:
    def __init__(self, maxsize=1):
        self.maxsize = maxsize
        self.cache = {}
        self.dll = DLL()

    def insertKeyValuePair(self, key, value):
        if key in self.cache:
            self.cache[key].value = value
            self.dll.update(self.cache[key])
            return
        node = Node(key, value)
        self.cache[key] = node
        self.dll.push(node)
        if self.dll.length > self.maxsize:
            del_node = self.dll.pop()
            del(self.cache[del_node.key])
            
    def getValueFromKey(self, key):
        if key in self.cache:
            node = self.cache[key]
            value = node.value
            self.dll.update(node)
            return value
        return None

    def getMostRecentKey(self):
        if self.dll.head:
            return self.dll.head.key
        return None

