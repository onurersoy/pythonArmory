numbers = set()
# This is how you initialize an empty set^^

print(numbers, type(numbers))

data = ["blue", "red", "blue", "green", "red", "blue", "white"]

# Create a set from the list above, to remove duplicate values:
unique_data = set(data)
print(unique_data)  # Now each colour appears once

# If you want the list in alphabetical order, you can use the 'sorted' function.
# The sorted function will take any iterable, and produce a list. So the output, when I run the program this time,
# is a list:
unique_data2 = sorted(set(data))
print(unique_data2)

# There is another way we can do this, which is useful if you need to keep the order that each colour was first spotted.
# It should be obvious that we can't use a set. Whenever you are interested in ordering, sets are automatically
# ruled out.

# Create a list of unique colours, keeping the order they appeared:
unique_data3 = list(dict.fromkeys(data))
print(unique_data3)
print()
print(dict.fromkeys(data))  # It creates a dictionary, removing duplicates and preserving the appearing order
print(list(dict.fromkeys(data)))  # Then converting to list, so it only holds the keys which is what we want (because
# values are already 'None' >> re-check 'dict.fromkeys' from the above section if you need)
