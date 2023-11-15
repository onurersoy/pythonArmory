name = input("What is your name?: ")
age = int(input("How old are you {0}?: ".format(name)))
# int function changes string data type to int data type, so we can print out an integer value instead of a string.
# But by doing that^^, our code may crash if we typr anything that can't be converted to int.
print(age)
