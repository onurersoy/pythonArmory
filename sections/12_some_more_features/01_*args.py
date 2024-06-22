# *args
# It lets a function or method take a variable number of arguments. For example, do 'command + left click' into print
# function and notice that '*args' there as a function parameter.

print("hello", "planet", "world")


# So our three string values are wrapped up in a tuple so args, or *args, is the unpacked values in that tuple.
# Args itself is a tuple, and the print function takes each item from the tuple and then prints it. Now as a result, it
# doesn't care how many arguments we provide, it just iterates over the tuple and prints them all.


def average(*args):
    print(type(args))  # tuple
    print(f"args is: {args}")  # the tuple itself
    print(f"*args is:", *args)  # the items of the tuple
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


# 'args' is the tuple while '*args' is the unpacked vaulues of the tuple.
print(average(1, 2, 3, 4))


# The first is the name args. Now you can use any name you want, as long as obviously it's a valid path and variable
# name. The convention now is to call it args, which is an abbreviation for arguments. Now unless you've got a very good
# reason, and frankly, I can't think of one, then stick to the convention. And that's because it makes it much easier
# for other people to read your code.

# The second is that a variadic parameter, as the documentation calls this, must appear after all other positional
# parameters. So there can be no parameter after *args.


# Challenge:
def built_tuple(*args):
    return args
    # So this function takes any number of given inputs and returns it as a tuple.


number_tuple = built_tuple(1, 2, 3, 4, 5, 6)
print(type(number_tuple))
print(number_tuple)

# '*' can also be used to unpack a list as well as a tuple.
