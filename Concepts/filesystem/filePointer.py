# if filecontent is like this and we want to extract the name
# Hi my name is Kajal
file = open("/home/kajal/Documents/Python-Revision/Concepts/filesystem/data/name.txt", "r")

file.readlines()
file.seek(0)
count = 0

#Python intentionally disables tell() in this situation for text files, because the iterator may use internal buffering.
for i in file:
    count += 1
    # print(count, file.tell()) #*here python intentionally disables file.tell() and uses the file's iterator mechanism (next()) to efficiently read the file.
    # if file.tell() == count:
    print(i)
file.close()

#Reading through split method
with open("/home/kajal/Documents/Python-Revision/Concepts/filesystem/data/name.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        name = line.split("name is")[1].strip()
        print(f"Hi {name}")



