#!/usr/bin/env python3

""" A script for LIFO caching"""

from Basic_Cache_Implementation import SimpleCache


class LIFOCache:
    """lifo cache implementation"""
    
    def __init__(self, capacity, cache):
        self.capacity = capacity
        self.cache = []
    
    def access(self, data):
        if len(self.cache) >= self.capacity:
            self.cache.pop()
        else:
            self.cache.append(data)
            
    def display_cache(self):
        print(self.cache)
            
        
lifocahe = LIFOCache(3, [1, 2])  
lifocahe.access("first")  
lifocahe.access("seconed")   
lifocahe.access("third")   
lifocahe.access("forth")   
lifocahe.access("fifth")   
lifocahe.access("sexth")   
lifocahe.access("seventh")   

   
lifocahe.display_cache()    