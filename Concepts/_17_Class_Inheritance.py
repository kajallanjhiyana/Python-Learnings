#Types of Inheritance
#!Single Inheritance
# When one child class inherits only one parent class, 
# it is called single inheritance.  

class Person:
    name = "Person"

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    name = "Student"

    def __init__(self):
        self.name = input("Enter name of the student: ")
        self.age = int(input("Enter Age of the student: "))
        
        super().__init__(self.name, self.age)
    
    def isStudent(self):
        print(f"{self.name} is a student")

# student = Student()
# student.isStudent()

#! Multiple Inheritance
# When one child class inherits two or more parent classes, it is called Multiple Inheritance. 
# Unlike Python, this feature is not supported in Java and C++.

class SuperClass1:
    num1 = 2

class SuperClass2:
    num2 = 3

class ChildClass(SuperClass1, SuperClass2):
    num3 = 4
    def __init__(self):
        print("self.num1 = ",self.num1, "self.num2 = ", self.num2, "self.num3 = ", self.num3)

obj = ChildClass()

#! Multilevel Inheritance
# When a class inherits a child class, it is called Multilevel Inheritance.
# The class which inherits the child class is called a grandchild class.
#  Multilevel Inheritance causes grandchild and child relationships. 
# The grandchild class has access to both child and parent class properties.

class Parent:
    str = "jhon"

class Child(Parent):
    str2 = "joe"

class GrandChild(Child):
    str3 = "july"

    def get_str(self):
        print("str1 = ", self.str, "str2 = ", self.tr2, "str3 = ", self.str3)

#! Hierarchical Inheritance
# When multiple classes inherit the same class, it is called Hierarchical Inheritance.

class Child1(Parent):
    name = "child1"

class Child2(Parent):
    name2 = "Child2"

class Child3(Parent):
    name3 = "Child3"

obj1 = Child1()
obj2 = Child2()
obj3 = Child3()
print(obj1.str, obj2.str, obj3.str)

#Hybrid Inheritance
# A combination of more than one type of inheritance is called Hybrid Inheritance.

class Parent1:
    str = "parent"

class Child(Parent1):
    str2 = "child"

class Child2(Parent1):
    str2 = "child2"

class GrandChild(Child, Child2):
    str3 = "grandchild"

