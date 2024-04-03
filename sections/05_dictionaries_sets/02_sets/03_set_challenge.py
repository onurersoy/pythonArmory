choice = "-"  # initialise choice to something invalid
while choice != "0":
    if choice in set("12345"):  # << testing for a membership
        # We used a 'list' to get rid of the bug we had while using a string.
        # Using a 'set' above also lets us get rid of the bug we had, but in the same our code is now very efficient
        # comparing with using a 'list.
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()

# You can use the 'set' function to create a new set.
# You pass any iterable object to it, and you'll get a set containing all the items in the iterable.
set(range(0, 20, 2))
