import sys

# Now because one of the advantages of generators is that they save memory - and actually a lot of memory in many
# cases - let's start by showing how we can check how much memory things use in Python.

big_range = range(1000)  # << This is a generator
print(f"The size of big_range is: {sys.getsizeof(big_range)}")

# Create a list containing all the values in big_range
big_list = []  # << This is a list
for value in big_range:
    big_list.append(value)
print(f"The size of big_list is: {sys.getsizeof(big_list)}")

# So what's actually going on here and how is there such a big difference in the memory that the two objects are using
# which actually stores exactly the same set of number? Well, both big_range and big_list are actually 'iterators', so
# we can use either in a for loop to iterate over all the values. Now big_range is a special case of an iterator called
# a 'generator', and in fact, we can run our own version of big_range.

# Notice the diff of memory usage!
