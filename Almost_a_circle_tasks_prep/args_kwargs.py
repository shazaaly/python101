

def printArhs(*args):
    for arg in args:
        print(arg)


printArhs("shaza", "printf", "shell")


def my_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


my_kwargs(name="shaza", email="shaza.aly@gmail.com")
