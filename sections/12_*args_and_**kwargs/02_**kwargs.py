# kwargs = keyword arguments

# def print_backwards(*args, file=None):
#     for word in args[::-1]:
#         print(word[::-1], end='', file=file)
#
#
# with open("backwards.txt", "w") as backwards:
#     print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", file=backwards)

# Now this is where the **kw args or kwargs actually comes in. We've seen that the asterix can be used to unpack a tuple
# or a list, but the double asterix operator, **, unpacks a dictionary in the same way.

# Now a dictionary is used because keyword arguments are specified as a keyword and a value, and that's exactly what you
# have in the dictionary, a key and a value. Find the refactored code below:

def print_backwards(*args, **kwargs):
    for word in args[::-1]:
        print(word[::-1], end=' ', **kwargs)


with open("backwards.txt", "w") as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", file=backwards)
# So **kwargs passes the keyword arguments to our method such as 'file=backwards' and many others as long as you want to
# provide it to your function. So you don't have to explicitly define them on your function but provide different number
# of keyword arguments to your each different function call. Sometimes there might be more than f.e. 20 keyword
# arguments that you may want to provide (and you can provide) depend on the function you use, f.e. print function etc.
# So this feature is a real saviour for these kinds of scenarios.

# Now once again, we could call a parameter anything, but the convention here is to use kw args or kwargs as the name
# (same like *args).
