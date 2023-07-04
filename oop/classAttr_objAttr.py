class Machine:
    count = 0

    def __init__(self, name, specs):
        self.name = name
        self.specs = specs
        Machine.count += 1


car_wash = Machine("Car Wash", "machine model 254dd")
print(car_wash.count)

car_wash2 = Machine("Car Wash", "machine model 254dd")
print(car_wash2.count)
