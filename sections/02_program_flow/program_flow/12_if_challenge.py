name = input("What is your name? ")
age = int(input("How old are you? "))

if 17 < age < 31:
    print("{} is free to pass".format(name))
else:
    print("{} is not allowed to pass".format(name))
