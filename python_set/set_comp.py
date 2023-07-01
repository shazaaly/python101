#!/usr/bin/python3
set_1 = {10, 20, 30, 40}
set_2 = {10, 20, 70, 80, 90}

set_1.add(32)
print(set_1)  # {32, 40, 10, 20, 30}

set_3 = set_1.difference(set_2)  # {32, 40, 30}#
print(set_3)

set_1.union(set_2)
print(set_1)  # {32, 40, 10, 20, 30}
# symmetric_difference():
# Returns a new set containing only the elements
# that are in either the original set or another set or iterable,
# but not in both.
dif = set_1.symmetric_difference(set_2)
print(dif)  # {80, 32, 90, 70, 40, 30}
