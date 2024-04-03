choice = "-"  # initialise choice to something invalid
while choice != "0":
    # if choice in set("12345"):
    if choice in {"1", "2", "3," "4", "5"}:  # << testing for a membership
        # Using a 'set literal', instead of the 'set' function ('03_set_challenge.py') is much faster.
        # After this simple change, the code performed twice as fast comparing with the 'set' function.

        # You might also decide to create the set once, outside the loop. Inside the loop, the 'valid_choices' variable
        # is used in the condition. We found very little performance difference between this code, and the code above.

        # Tight loop is one that iterates many times, and has a significant impact on the total execution time.
        # Those are the kinds of loops that can benefit from more efficient ways of writing the code.
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

# Why using 'in' with a set is faster than when you use a list?:
# The reason is that sets use hash codes - just like keys in a dictionary.

# When we check if something is in a list, Python has to check each item in the list, until it finds the one we want.
# If the item we check doesn't even exist in the list, Python firstly has to check each single item to tell that
# it is not in the list. That's called a 'linear search'. You start at the beginning, and check each item until you
# either find the one you want, or reach the end of the list.
# Note that this is the case even with a 'sorted list'. Python has no way to tell if a list is sorted, and has to
# perform a linear search when checking if something is in a list or not.
# When checking for a membership of a set, Python uses the hash code to find out where the item should be.
# If it's there, then the item is 'in' the set; otherwise it's not.
# Hash codes are used in the same way as we saw for dictionary keys.

# A hash code lets us go directly to the item in the hash table.
# There's a small overhead while the hash code is calculated, but once that's done, access is very fast.

# You can check if a value is in a set of one billion items, just as quickly as in a set of five items.
# The size of the set has no effect on the time taken, to check if something's in it.
# So that's the advantage of using a set, rather than a list, when testing for membership.
# If you are working with large data, checking for membership will be a lot faster with a set, compared to a list.
