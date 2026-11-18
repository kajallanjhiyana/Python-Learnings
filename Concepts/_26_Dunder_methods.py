# Dunder means Double Underscore.

# __init__()
# __str__()
# __repr__()
# __len__()
# __eq__()
# __add__()

# These are called special methods because Python automatically calls them when you perform certain operations.

students = {}
class Admission:
    __school_name = "AECS Narora"
    def __init__(self, name, age, section):
        self.name = name
        self.age = age
        self.section = section


    def __str__(self):
        return f"Welcome to {self.__school_name}"

    def __repr__(self, other):
        return self.__school_name

