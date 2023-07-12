with open("hello.txt", "r") as file:
    file.seek(10)
# read the contents of the file from the current cursor position
    content = file.read(-1)
    print(content)

