#!/usr/bin/python3

fruits = set(["millons", "orange", "apple"])  # set expects iterable
my_fruits = {"millons", "orange", "apple"}
print(fruits)
print(my_fruits)
# operations

a = {"Alx", "python", "sets"}
b = {"Alx", "python", "Dictionaries"}
print(a - b)  # a not b
print(a | b)
print(a ^ b)  # a or b not in both
