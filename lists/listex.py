import math

evenLists = [i * 2 for i in range(5)]
print(evenLists)

for i in evenLists:
    print(i)

new = [[math.pow(m, 2), math.pow(m, 2),math.pow(m, 2),math.pow(m, 2),math.pow(m, 2)] for m in evenLists]
for i in new:
    print(i)