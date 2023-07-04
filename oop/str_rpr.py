class Machine:
    def __init__(self, name, specs):
        self.name = name
        self.specs = specs

    def __str__(self):    # string representation of an object
        return f"{self.name}, {self.specs}"

    def __repr__(self):
        # info needed to recreate the object: type and all its attributes.
        return f"Machine(name='{self.name}', specs = '{self.specs}')"


dishwasher = Machine("GMC", "washing machine model : gf12545")
# GMC, washing machine model : gf12545:
print("str method call: ", str(dishwasher))

# Machine(name='GMC', specs = 'washing machine model : gf12545') :
print("repr method call :  ", repr(dishwasher))
