class User:
    _age = 9
    __brother_age = 90
    def __init__(self):
        print("hey user your age is ", self._age)
    
    #A getter is a method used to get or read the value of a variable.
    def get_age(self):
        return self._age

    def get_brother_age(self):
        return self.__brother_age

    #A setter is a method used to modify or update the value of a variable, usually with validation.
    def set_brother_age(self, new):
        if new >0:
            self.__brother_age = new
        elif new <0:
            print("Age cannot be a negative number.")
        else:
            print("Age can't be zero")

    def set_age(self, new):
        if new >0:
            self._age = new
        elif new <0:
            print("Age cannot be a negative number.")
        else:
            print("Age can't be zero")

obj = User()
print("obj._age = ",obj._age)
age = obj.get_age()
print("obj.get_age = ", age)
obj.set_age(16)
print("obj._age = ",obj._age)
print("obj.get_age = ", obj.get_age())

#accessing brother's age
print("obj._age = ",obj._User__brother_age)
age = obj.get_brother_age()
print("obj.get_brother_age = ", age)
obj.set_brother_age(22)
print("obj._brother_age = ",obj._User__brother_age)
print("obj.get_brother_age = ", obj.get_brother_age())

