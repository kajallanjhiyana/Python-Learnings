#@property allows us to call a method like an ordinary variable (attribute).

class User:
    _age = 9
    def __init__(self):
        print("hey user your age is ", self._age)
        self._age = 80

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new):
        if new >0:
            self._age = new
            print("age is set")
        elif new <0:
            print("Age cannot be a negative number.")
        else:
            print("Age can't be zero")

obj = User()

#!getter
print(obj.age)

#!setter
obj.age = -9
print(obj.age)

obj.age = 10
print(obj.age)