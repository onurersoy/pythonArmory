import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please try again")
        except EOFError:
            sys.exit(1)
        finally:
            print("The finally clause always executes")
        # Finally clause:::
        # A 'Finally Clause' is followed by the block of code that you want to execute whether an exception was raised
        # or not. A 'Finally Claus' must come after all your 'except clauses' and remember that it always executes.
        # It's still even getting executed after a program finisher code like: "sys.exit(1)".

first_number = getint("Please enter first number ")
second_number = getint("Please enter second number ")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("You can't divide by zero")
    sys.exit(2)
