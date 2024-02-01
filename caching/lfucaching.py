#!/usr/bin/env python3

""" A script for LFU caching"""
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity  # Maximum number of items the cache can hold
        self.vals = {}  # Maps keys to their values
        self.counts = {}  # Maps keys to their access frequencies
        self.lists = {0: []}  # Maps frequencies to lists of keys with that frequency
        self.minCount = 0  # The minimum access frequency of any key in the cache

    def update(self, key: int):
        """Update the frequency of a key upon access."""
        count = self.counts[key]  # Get the current frequency of the key
        self.counts[key] = count + 1  # Increment the key's frequency
        
        # Remove the key from its current frequency list
        self.lists[count].remove(key)
        # If this was the only key with the lowest frequency and the list is now empty, increment minCount
        if count == self.minCount and not self.lists[count]:
            self.minCount += 1
        
        # Add the key to the list of the next frequency
        if count + 1 not in self.lists:
            self.lists[count + 1] = []  # Create the list if it doesn't exist
        self.lists[count + 1].append(key)  # Add the key to its new frequency list

    def get(self, key: int) -> int:
        """Retrieve the value of the key if present, and update its frequency."""
        if key not in self.vals:
            return -1  # Key not in cache
        self.update(key)  # Update the frequency since the key is accessed
        return self.vals[key]  # Return the value of the key

    def put(self, key: int, value: int):
        """Add or update a key with a given value."""
        if self.capacity <= 0:
            return  # Do nothing if the cache capacity is 0
        
        if key in self.vals:
            # If the key exists, just update its value and frequency
            self.vals[key] = value
            self.update(key)
            return
        
        if len(self.vals) >= self.capacity:
            # Cache is full, need to evict the least frequently used key
            evict = self.lists[self.minCount][0]  # Choose the oldest key with the minimum frequency
            self.lists[self.minCount].pop(0)  # Remove it from the list
            del self.vals[evict]  # Remove it from vals
            del self.counts[evict]  # Remove its frequency count
            
        # Add the new key-value pair to the cache
        self.vals[key] = value  # Insert the key with its value
        self.counts[key] = 1  # Set its frequency to 1
        if 1 not in self.lists:
            self.lists[1] = []  # Create the list for frequency 1 if it doesn't exist
        self.lists[1].append(key)  # Add the key to the list for frequency 1
        self.minCount = 1  # Reset minCount to 1 as we've added a new key with frequency 1
