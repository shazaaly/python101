mylist = ["1", "2", "3", 104, 555, "Apple"]
x = 5
counter = 0

try:
    for item in mylist:
        counter = counter + 1
        if counter <= x:
            print(f"{item}")
        else:
            break
except ValueError:
    print("x must be <= list elements count")