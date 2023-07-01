class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
        self.__address = None

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    def speak(self):
        print(f"Hello, my name is {self.name}. I'm {self._age} years old.")

    def __str__(self):
        return f"{self.name} ({self._age})"

    def __repr__(self):
        return str(self)


person1 = Person("John", 30)
person1.speak()  # Output: Hello, my name is John. I'm 30 years old.

person1.set_age(35)
print(person1.get_age())  # Output: 35

person1.address = "123 Main St"
print(person1.address)  # Output: 123 Main St

person1.new_attribute = "This is a new attribute"
print(person1.new_attribute)  # Output: This is a new attribute

print(person1.__dict__)
print(Person.__dict__)
print(getattr(person1, "name"))  # Output: Johns
