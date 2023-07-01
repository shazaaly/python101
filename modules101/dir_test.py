class Student:
    def __int__(self):
        self.name = "John Albert"

    def active(self):
        print("John is active!")


obj = Student()
print("local dir: ", dir())
print("obj argument in dir: ", dir(obj))

