with open("/home/kajal/Documents/Python-Revision/Concepts/filesystem/my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("/home/kajal/Documents/Python-Revision/Concepts/filesystem/my_file.txt", mode = "a") as file:
    file.write("\nhi")