# Dunder means Double Underscore.

# __init__()
# __str__()
# __repr__()
# __len__()
# __eq__()
# __add__()

# These are called special methods because Python automatically calls them when you perform certain operations.

students = [{
    "name" : "Saniya",
    "age" : 16,
    "section": 10
}]
class Admission:
    __school_name = "AECS Narora"
    def __init__(self, name, age, section):
        self.name = name
        self.age = age
        self.section = section

    def __str__(self):
        return f"Welcome to {self.__school_name}"

    def __repr__(self):
        return self.__school_name

    def add(self):
        students.append({"name": self.name, "age": self.age, "section": self.section})

    def tc(self):
        students.remove({"name": self.name, "age": self.age, "section": self.section})

    def __len__(self):
        return len(students)

class Student(Admission):

    def __init__(self, student):
        print("Welcome student to the class!")
        self.student = student
        super().__init__(student.name, student.age, student.section)
    
    def __str__(self):
        # print(self.student)
        # return self.student #!this will give error because it a object it should be string
        return f"name = {self.student.name} age = {self.student.age}, section = {self.student.section}"

    def __eq__(self, other):
        return self.student == other

golu = Admission("golu", 15, 5)
print(golu)
golu.add()
print("School strength = ", len(golu))
golu2 = Student(golu)
print(golu2)


priya = Admission("Priya", 17, 6)
print(priya)
priya.add()
print("School strength = ", len(priya))
priya = Student(priya)
print(priya)

print(priya == golu2)
print(len(priya) == len(golu2))