# Day 2 — Control Flow
# if/elif/else, for and while loops, break/continue/pass, range(), enumerate(), zip(). Pairs with: Single Number, Intersection of Two Arrays II.

names = []
marks = []
grades = []

# Step 1: keep asking until the number is valid
while True:
    text = input("Enter number of students: ")
    if not text.isdigit() or int(text) <= 0:
        print("Invalid number, try again.")
        continue
    num = int(text)
    break

# Step 2: collect data and assign grades
for i in range(num):
    name = input(f"Enter name for student {i + 1}: ")
    if name == "STOP":          # check BEFORE appending anything
        break

    mark = int(input(f"Enter marks for student {i + 1}: "))
    if mark < 0 or mark > 100:
        print("Invalid marks, skipping")
        continue                # skip this student completely

    if mark >= 90:
        grade = "A"
        pass                    # TODO: add to Honors List later
    elif mark >= 75:
        grade = "B"
    elif mark >= 50:
        grade = "C"
    else:
        grade = "D"

    names.append(name)
    marks.append(mark)
    grades.append(grade)

# Step 3: print the report
print("--- Report Card ---")
for sno, (name, mark, grade) in enumerate(zip(names, marks, grades), start=1):
    print(f"{sno}. {name} - {mark} - Grade: {grade}")

