# There are 3 methods we can use that can delete items from a set.
some_ints = set(range(30))
print(some_ints)

some_ints.clear()  # It removes all the items in the set and leaves an empty set.
print(some_ints)

print()

small_ints = set(range(21))
print(small_ints)
small_ints.discard(10)  # It removes the item '10'
small_ints.remove(11)  # It removes the item '11'
print(small_ints)

small_ints.discard(99)  # It removes the item '99' if exists; if not, then nothing happens
# Ensure that, when we're done, something no longer exists. In this case, we don't care if it was already there or not,
# we just want it gone.
print(small_ints)
small_ints.remove(100)  # It removes the item '100' if exists; if not, you get an error
# Remove something if it exists, but provide some sort of notification if it doesn't.
# You don't care if something is in the set or not - you just want to make sure it's not there, after the code has
# executed.
print(small_ints)
