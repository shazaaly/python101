#!/usr/bin/env python3

""" A script for LRU caching"""


from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = 3
        self.cache = OrderedDict()
        
    def get(self, key):
        """ get cached data by key """
        if key in self.cache:
            self.cache.move_to_end(key)
            print(self.cache[key])
        return -1
    
    def put(self, key, value):
        """ set key value in cache """
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value
            
                
        
        
lru = LRUCache(3)
lru.put('item1', 1)
lru.put('item2', 2)
lru.put('item3', 3)
lru.put('item3', 4)



lru.get('item1')
lru.get('item2')
lru.get('item3')
lru.get('item4')