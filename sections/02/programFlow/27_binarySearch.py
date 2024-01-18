# Binary Search algorithm == Binary Chop
# An algorithm is a set of steps that are followed, to perform a task or calculate a result.

low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
while True:  # Since True is always True, it will keep iterate in this 'while' loop, until the conditions met and find
    # the 'break' line.

    print("\tGuessing in the range of {} to {}".format(low, high))  # To test our code <<<

    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if my guess was correct "
                     .format(guess)).casefold()

    if high_low == "h":
        # NOTE: In this example, after 'if', you will see the error 'indent expected' since a comment doesn't count.
        # What you can do here is adding a dummy bit of code inside the indented block, to clear this error. So
        # there's a specific keyword in Python for that and that's called 'pass'. Now 'pass' doesn't do anything,
        # but it makes the code syntactically correct.

        # pass
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes one less than the guess.

        # pass
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")

    # guesses = guesses + 1
    # Let's refactor above^^:
    guesses += 1

# PS. Please remember that Python doesn't have a case or switch statement.
