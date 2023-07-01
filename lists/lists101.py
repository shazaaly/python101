
import random
import math

randList = ["string", 20.36, 28, "book"]
tri = randList[:3]

for element in tri:
    print("{} : {}".format(tri.index(element), element))
print(randList[0] * 3)

if "string" in tri:
    print("{} is the index of \"string\"".format(tri.index("string")))

my_list = [1, 2, 3, 4, 5, 3]
print("{} count {} times in the list".format(my_list[2], my_list.count(my_list[2])))

my_list.append("Final")
print(my_list)