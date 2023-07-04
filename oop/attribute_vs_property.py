class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    @property
    def car_desc(self):
        print("Car Specs: ", self.brand, self.color)


car_01 = Car("bmw", "red")
car_01.car_desc   # not Car.car_desc() to avoid TypeError:
# 'property' object is not callable

