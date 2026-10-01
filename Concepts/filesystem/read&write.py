# Open the file in "r" (read) mode.
# "file" is a file object that lets us interact with the file.
file = open("/home/kajal/Documents/Python-Revision/Concepts/filesystem/data/name.txt", "r")

# readlines() reads ALL lines from the file
# and returns them as a list of strings.
#! IMPORTANT:
#! Reading the file moves the file pointer to the END of the file.
print(file.readlines())

# It prints information about the file object,
# such as its memory location and mode.
print(file)

# BUT: readlines() above has already moved the file pointer
# to the end of the file.
# Therefore, there is nothing left for this loop to read,
# so this loop will print NOTHING.
for i in file:
    print(i)

#it tells the pointer to go back to the beginning of the file.
file.seek(0)
for i in file:
    print(i)

# "with open()" is preferred because Python automatically
# closes the file when the block is finished.
# Since no mode is specified, the default mode is "r" (read).
with open("/home/kajal/Documents/Python-Revision/Concepts/filesystem/data/my_file.txt") as file:
    contents = file.read()
    print(contents)

# Open my_file.txt in "a" (append) mode.

# Append mode means:
# - Existing content is NOT deleted.
# - Anything we write is added to the END of the file.
with open("/home/kajal/Documents/Python-Revision/Concepts/filesystem/data/my_file.txt", mode = "a") as file:
    file.write("\nhi")


