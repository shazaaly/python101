class Person:
    def say_hello(self):
        print("Hello")


p = Person()
print(p.say_hello())


class Employer:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def takeAttendance(self):
        print("take Attendance")


staff = Employer("Jeson", 56)

print(staff.name)
print(staff.age)
print(staff.takeAttendance())
