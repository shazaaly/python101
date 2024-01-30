#!/usr/bin/env python3

""" A script for simple caching"""

from collections import deque

class SimpleCache:
    """ A class to implement Cache"""
    
    def __init__(self):
        """cache method"""
        self.cache = deque()
        
       
    def display(self):
        print(list(self.cache))
        
        