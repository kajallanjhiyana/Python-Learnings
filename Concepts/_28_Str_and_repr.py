
class Student:

    v = "hi125@"  # Class variable

    def __init__(self, name):
        self.name = name
        print(f"Hey {self.name}")

    def __str__(self):
        # Returns a user-friendly string representation
        return f"Student's name is {self.name}"

    def __repr__(self):
        # Returns a developer-friendly representation
        return f"Student(name={self.name!r})"


obj = Student("Riya")

print("obj =", obj)

# Explicitly calls __str__()
print("str(obj) =", str(obj))

# Explicitly calls __repr__()
print("repr(obj) =", repr(obj))

print(str(obj) == obj)
print(type(str(obj)))
print(type(obj))

