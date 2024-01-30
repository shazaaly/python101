#!/usr/bin/env python3

""" A script for simple caching"""

class SimpleCache:
    """ A class to implement Cache"""
    
    def __init__(self):
        """cache method"""
        self.cache = {}
        
    def get(self, key):
        return self.cache.get[key]
    
    def set(self, key, value):
        self.cache[key] == value
        
    def display(self):
        print(self.cache)
        
        