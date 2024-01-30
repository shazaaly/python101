#!/usr/bin/env python3

""" A script for FIFO caching"""

from Basic_Cache_Implementation import SimpleCache

class FIFOCache(SimpleCache):
    """ A class to implement FIFO Cache"""
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity
        
    def access(self, data):
        """ a method to chech data in cache """
        if data not in cache:
            if len(cache) >= capacity:
                self.cache.popleft()
               
            self.cache.append(data)
    def show_cache(self):
        self.display()
        
                
        