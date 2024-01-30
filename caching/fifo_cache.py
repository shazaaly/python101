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
        if data not in self.cache:
            if len(self.cache) >= self.capacity:
                self.cache.popleft()
               
            self.cache.append(data)
            
    def show_cache(self):
        self.display()
    
    
# test
fifo_cache = FIFOCache(3)
fifo_cache.access("Hello 1")
fifo_cache.access("Hello 2")
fifo_cache.access("Hello 3")
fifo_cache.access("Hello 4")
fifo_cache.access("Hello 5")
fifo_cache.access("Hello 6")
fifo_cache.access("Hello 7")
fifo_cache.access("Hello 8")
fifo_cache.access("Hello 10")
fifo_cache.access("Hello 11")
fifo_cache.access("Hello 12")
fifo_cache.show_cache()

                
        