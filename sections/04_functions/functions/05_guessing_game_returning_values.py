import random


def get_integer(prompt):
    while True:  # Because we do not have an input yet
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)  # Return will make while loop to stop
        else:  # If the input is not numeric, code never goes to return line, so you don't even need this 'else' line.
        # print("{} is not a valid number.".format(temp))  # You could've directly add like this!
            print("You have provided an invalid value, try again:")


highest = 1000
answer = random.randint(1, highest)
print(answer)  # For testing purposes
guess = 0  # Initialise to any number that doesn't equal to the answer
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
