if 0: # 0 is evaluated to False when it appears in a boolean expression
    print("True")
else:
    print("False")

name = input("Please enter your name: ")
if name: # if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")
