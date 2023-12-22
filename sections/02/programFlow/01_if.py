name = input("What is your name?: ")
age = int(input("How old are you {0}?: ".format(name)))
# int function changes string data type to int data type, so we can print out an integer value instead of a string.
# But by doing that^^, our code may crash if we type anything that can't be converted to int.
print(age)

if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Please come back in {0} years".format(18 - age))

if age < 18:
    print("Please come back in {0} years".format(18 - age))
else:
    print("You are old enough to vote")
    print("Please put an X in the box")
