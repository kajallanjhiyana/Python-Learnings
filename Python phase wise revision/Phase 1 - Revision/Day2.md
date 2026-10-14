Requirements:

Use a while loop to repeatedly ask "Enter number of students:" until the user enters a valid positive whole number.
If the input isn't a valid number, or is zero/negative, print an error and loop again (continue)
Once valid, exit the loop (break)
Use a for loop with range() to collect that many students' names and marks into two separate lists (names = [], marks = []).
Use zip() to pair the names and marks lists together for processing.
Use enumerate() on the zipped pairs so you can print a serial number (1, 2, 3...) alongside each student's report line.
Inside that loop, use if/elif/else to assign a grade based on marks:
90 and above → Grade A
75–89 → Grade B
50–74 → Grade C
Below 50 → Grade D
Use continue: if a student's marks are negative (invalid data), print "Invalid marks, skipping" and move to the next student without assigning a grade.
Use break: if a student's name is exactly "STOP", stop generating the report immediately — don't process that student or anyone after them.
Use pass: wherever a student gets Grade A, leave a placeholder comment for a feature you haven't built yet — e.g., adding them to an "Honors List" — using pass so the code runs without errors even though that feature isn't implemented.
Example Input
Enter number of students: -2
Invalid number, try again.
Enter number of students: abc
Invalid number, try again.
Enter number of students: 4

Enter name for student 1: Asha
Enter marks for student 1: 95

Enter name for student 2: Ravi
Enter marks for student 2: 60

Enter name for student 3: Neha
Enter marks for student 3: -10

Enter name for student 4: STOP
Enter marks for student 4: 0
Example Output
--- Report Card ---
1. Asha - 95 - Grade: A
2. Ravi - 60 - Grade: C
Invalid marks, skipping
--- Report generation stopped early ---