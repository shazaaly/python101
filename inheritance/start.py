class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, stage):
        super().__init__(name, age)
        self.stage = stage


stud = Student("Faith", 9, "Primery 3")
print(stud.stage)
print(issubclass(Student, Person))
