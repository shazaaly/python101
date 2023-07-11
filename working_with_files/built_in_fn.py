
my_file = open("hello.txt", "r")
my_file.close()

with open("hello.txt", "w") as my_file:
    my_file.write("https://twitter.com/ShazaAlyOthman\n")


with open("hello.txt", "a") as my_file:
    my_file.write("Alx inspired SW engineer \n")

