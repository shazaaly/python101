with open("hello.txt", "r") as file:
    # This will open the file in read mode and create a
    # loop that will continue as long as there are lines
    # to read in the file.
    line = file.readline()

    while line:
        # This will read the next line from the file
        # and remove any whitespace from the beginning
        # and end of the line.
        line = line.strip()

        # This will print the line to the console.
        print(line)

        # This will get the next line from the file.
        line = file.readline()

    # This will close the file.
    file.close()
