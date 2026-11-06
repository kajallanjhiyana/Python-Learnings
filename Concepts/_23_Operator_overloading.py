# Operator overloading means using the same operator with different types of objects to perform different operations.

class Family:
    family = ["Mom", "Dad", "Son"]
    def __init__(self):
        print("Welcome to family")

    def __add__(self, new_mem):
        self.family.append(new_mem)
        print(self.family)

Mom = Family()
print(Mom + "Daughter")
