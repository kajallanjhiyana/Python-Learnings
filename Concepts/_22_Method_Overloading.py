# Method overloading means having multiple methods with the same name but different parameters.

def Add(a, *numbers):
    print(numbers)
    s = a
    for i in range(0, len(numbers)):
        print(numbers[i])
        s += numbers[i]
    print("sum = ", s)

Add(12, 13, 14, 15)
print()

