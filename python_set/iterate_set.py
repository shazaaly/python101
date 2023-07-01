nums = {1, 2, 3, 4, 5, 6, 7, 8}

for x in nums:
    print(x)  # prints each element on a separate line.

even = {i for i in nums if i % 2 == 0}
print(even)  # resulting set contains only even members.
