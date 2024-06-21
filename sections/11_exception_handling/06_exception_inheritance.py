# Exceptions like everything else in Python are objects in Python 3, they must be derived from the base exception
# class or one of its subclasses. So instead of using its subclasses, it's possible to use one level high baseclass
# which is 'Exception'. But it's mostly a better practice to handle different type of errors (exceptions) separately.
# Now check line 14.

import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        # More specific exceptions must appear first so let's change the order of Exception - EOFError to EOFError -
        # Exception:
        except EOFError:
            sys.exit(1)
        except Exception:
            print("Invalid number entered, please try again")
        finally:
            print("The finally clause always executes")

first_number = getint("Please enter first number ")
second_number = getint("Please enter second number ")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("You can't divide by zero")
    sys.exit(2)
else:
    print("Division performed successfully")
    # Else must come after all the 'except clauses' and right before a 'finally clause'. Notice that it won't be
    # executed if the program catches any exception.
