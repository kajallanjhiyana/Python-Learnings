class Bird:
    pass

class Peacock(Bird):
    pass

class Animal:
    pass

class SunBird(Bird):
    pass

class Cat(Animal):
    pass

obj = Cat()
print(isinstance(Cat, Bird)) #True
print(issubclass(Cat, Bird)) #True
print(isinstance(obj, Animal)) #False
print(issubclass(Cat, Animal)) #False