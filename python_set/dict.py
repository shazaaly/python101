grades = {
    "Precious": 50,
    "Edward": 70,
    "Shaza": 75,
    "Eric": 33
}

my_grades = dict([('Math', 20), ('Physics', 25), ('Arabic', 50)])
french = my_grades["french"] = 100
print(grades["Edward"])  # 70
print(my_grades["Physics"])  # 25
print(my_grades.get("Arabic"))  # 50
print(french)  # 100
print(list(grades))
print(sorted(grades))
print("Eric" in grades)
print("Eric" not in grades)
print(sorted(grades))
