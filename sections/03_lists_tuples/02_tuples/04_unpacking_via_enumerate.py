for index, character in enumerate("abcdefgh"):
    print(index, character)

# Let's re-create the above with only one value:
for t in enumerate("abcdefgh"):
    print(t)
    # If you notice, it 't' holds the value of both, and it is a tuple!

# Now let's put it this way:
for t in enumerate("abcdefgh"):
    index, character = t  # Let's unpack the tuple
    print(index, character)
    # Notice that it's the same thing with the above one

index, character = (0, 'a')
print(index)
print(character)
