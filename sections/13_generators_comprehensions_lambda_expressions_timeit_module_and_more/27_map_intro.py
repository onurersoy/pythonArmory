# Python's got some built-in functions that can be used as an alternative to comprehensions. Generally, I suggest using
# comprehensions instead, and in fact Guildo van Rossum wanted to remove map and filter from Python altogether, but was
# instead persuaded to keep them.

text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]
print(capitals)

words = [word.upper() for word in text.split(' ')]
print(words)
# Now the program above uses 2 comprehensions as we are familiar with these examples from the previous modules.
# We can do the same thing with map function.

# using map
map_capitals = list(map(str.upper, text))
print(map_capitals)

# using map
map_words = list(map(str.upper, text.split(' ')))
print(map_words)
# PS. Remember that when passing a function as an argument, you don't include the opening and closing parentheses.
# When you use parentheses, you're passing the result of calling the function, but here we want to pass the function
# itself.
# PS. The second argument's an iterator. You can use anything that can be iterated over, such as a string or a list. So
# map_capitals is using the string text and map iterating over each character in the string and calls the str.upper
# function for each one. It then builds up another iterable which we convert to a list. Map_words is doing the same
# thing but creates an iterable by splitting the text into words. Split returns the list, remember, so the split list
# is an iterable that map's iterating over, and that's basically what map does. It calls the function for each item in
# the iterable and stores the result in a new iterable.

# So we've used that iterable to create a list, but we could have, instead, just iterated over it:
for x in map(str.upper, text.split(' ')):
    print(x)
# So is there anything to be gained from using 'map' instead of a comprehension? In my opinion, I'd say there isn't.
# The comprehension is easier to write and more importantly, easier to read. It's just more obvious what they're
# doing, which was Guido's main reason for wanting to remove 'map' from Python 3.
