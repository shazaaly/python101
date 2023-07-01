my_list = [1, 2, 3]

# append(item)
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# extend(iterable)
my_list.extend([5, 6, 7])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7]

# insert(index, item)
my_list.insert(1, 10)
print(my_list)  # Output: [1, 10, 2, 3, 4, 5, 6, 7]

# remove(item)
my_list.remove(2)
print(my_list)  # Output: [1, 10, 3, 4, 5, 6, 7]

# pop([index])
item = my_list.pop(3)
print(item)      # Output: 4
print(my_list)   # Output: [1, 10, 3, 5, 6, 7]

# index(item)
index = my_list.index(5)
print(index)  # Output: 3

# count(item)
count = my_list.count(10)
print(count)  # Output: 1

# sort()
my_list.sort()
print(my_list)  # Output: [1, 3, 5, 6, 7, 10]

# reverse()
my_list.reverse()
print(my_list)  # Output: [10, 7, 6, 5, 3, 1]

# len(list)
length = len(my_list)
print(length)  # Output: 6
