
import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def birth_date(cls, name, birthyear):
        age = datetime.date.today().year - birthyear
        return cls(name, age)

    @staticmethod
    def print_welcome_msg():
        return "Welcome press any key to cont..."


print(Person.print_welcome_msg())

student1 = Person("Ahmed", 30)
student2 = Person.birth_date("ibram", 1990)
print(student1.age)
print(student2.age)

