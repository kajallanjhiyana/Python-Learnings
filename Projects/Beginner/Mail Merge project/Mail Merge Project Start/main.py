#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("/home/kajal/Documents/Python-Revision/Projects/Beginner/Mail Merge project/Mail Merge Project Start/Input/Names/invited_names.txt", "r") as file:
    names = file.readlines()
    # print(names)
    # for i in names:
    #     print(i)

with open("/home/kajal/Documents/Python-Revision/Projects/Beginner/Mail Merge project/Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as file: 
    contents = file.read()
    for i in names:
        striped_name = i.strip()
        print("i =", i, "stripped_name = ", striped_name)
        new_letter = contents.replace("[name]", striped_name)
        with open(f"/home/kajal/Documents/Python-Revision/Projects/Beginner/Mail Merge project/Mail Merge Project Start/Output/ReadyToSend/{i}.txt", "w") as file2:
            file2.write(new_letter)
        
