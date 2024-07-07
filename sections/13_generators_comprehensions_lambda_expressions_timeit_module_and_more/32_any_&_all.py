# 'All', that checks to see if the items in an iterable are true.
# 'Any', by contrast, checks to see if any of them are.
# Both functions take an iterable and return either true or false, depending on the values in the iterable.

entries = [1, 2, 3, 4, 5]
print(f"all: {all(entries)}")  # All the values in the above list true
print(f"all: {any(entries)}")  # Any of the values in the above list true

# Now remember that 0, 0.0, empty list, empty tuple, empty string, empty mapping are False in Python.
print("Iterable with a 'False' value:")
entries_with_zero = [1, 2, 0, 4, 5]
print(f"all: {all(entries_with_zero)}")  # False
print(f"all: {any(entries_with_zero)}")  # True

entries2 = []
# print("all: {}".format(all(entries2)))  # << This one is surprisingly True, so it's better to use it like this:
if entries2:
    print("all: {}".format(all(entries2)))
else:
    print(False)
print("any: {}".format(any(entries2)))  # False
