import random
listr = []

for i in range(5):
    listr.append(random.randrange(1,5))
print(listr)
#[1, 4, 3, 3, 1]

count = len(listr) - 1
while count > 1:
    j = 0
    while j < count:
        if listr[j] > listr[j + 1]:
            tmp = listr[j]
            listr[j] = listr[j + 1]
            listr[j + 1] = tmp

        j += 1
        print(listr)
        print("END OF ROUND")

    count -= 1

for el in listr:
    print(el, end=", ")


