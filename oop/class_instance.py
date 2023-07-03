#!/usr/bin/python3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello {}".format(self.name))


employee1 = Person("Shaza", 69)
employee1.say_hello()

employee2 = employee1
print(employee2.name)
