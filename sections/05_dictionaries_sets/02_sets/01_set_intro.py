# 'Sets' are the last of Python's built-in data structures that we will be looking this section.
# A set is an unordered collection with no duplicate entries.
# A set is just a collection of items.

# The keys of a dictionary are very similar to a set. The main difference, since Python 3.7, is that dictionary keys
# are ordered.
# Sets have no ordering. That's why you can't do certain things with sets. F.e. There is no way to access individual
# elements of a set.

# We test for membership using the 'in' keyword. We've seen that with lists, tuples and dictionaries, and it works the
# same with sets.

# The 'union' of two or more sets is the set of all items that exist in all the sets.
# The elements of a set are unique. That's part of the definition of a set.
# An item might appear in both sets, but they only appear once in the union set.

# That property of sets - that the items are unique can be useful in our code. Converting a list to a set f.e will
# automatically remove any duplicate values.

# We can find the intersection of two sets (kesişim kümesi)
# We can subtract one set from another (A fark B kümesi gibi)
# Set theory also defines a symmetric difference. The symmetric difference is the set of items that are in one set
# or the other, but not both (A birleşim B'den kesişimlerinin çıkarılması). It's the opposite of intersection.

# One set can also be a subset of another set.
# There are also supersets.
