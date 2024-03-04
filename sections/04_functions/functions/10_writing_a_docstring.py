import random


def get_integer(prompt):  # Put """""" to the below line then press 'enter' in the middle of the characters
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting the user, until a valid `int` is entered.

    :param prompt: The String that the user will see, when they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    # ` = Backtick
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("You have provided an invalid value, try again:")


# 1st:
print(input.__doc__)  # '__doc__' is an attribute of 'input' method; it refers to docstring!
# It's not useful as you could simply hover over / or control+J the method to see its docstring (documentation)
print("*" * 80)
print(get_integer.__doc__)
print("*" * 80)

# 2nd:
help(get_integer())  # You can also use 'help' to check a method's docstring. It's actually a better alternative
# comparing with the 1st one.

highest = 1000
answer = random.randint(1, highest)
print(answer)  # For testing purposes
guess = 0
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
