# In this section, we learnt about two more Python built-in data structures – dictionaries and sets.

# Dictionaries and sets aren’t sequence types, unlike lists and tuples, so we can’t access individual items by using
# indexing.

# We use a unique key to get values from the dictionary, because they store key/value pairs. Each value is associated
# with a key, and the key is used to retrieve the value.

# Dictionaries are also referred to as mappings.
# There's no way to access a specific item from a set, but they can be very useful.

# We saw several ways to retrieve values from a dictionary:
# We can specify the key, by enclosing it in square brackets after the dictionary name. This is the fastest way to
# retrieve an item, but will give an error if the key doesn't exist. The get method will retrieve a value associated
# with a key, and doesn't crash if the key isn't present in the dictionary.
# '.get' returns None, by default, but we can provide a different value to return when the key doesn't exist.

# Dictionary keys are unique, and only hashable objects can be used as keys. One requirement to be hashable is that
# the object must be immutable. Lists, for example, can't be used as keys. Tuples can, but there are some
# restrictions – the tuple must not contain any mutable objects.

# This same requirement, that the object must be hashable, also applies to objects that we can put into a set.
# If you want a set that contains other sets, you have to use frozenset. We didn't show an example of a frozenset,
# but referred to the documentation about them. They're an immutable version of a set, and work in the same way as a set
# (except for adding or deleting items, of course).

# We saw how to iterate over the keys in a dictionary, and the items in a set.
# When iterating over a dictionary, you might want to retrieve the values at the same time. We used the items() method
# to do this. You can think of items() as the dictionary equivalent of using enumerate with a list.

# Iterating over .items() is an efficient way to retrieve the keys and values of a dictionary. It returns an iterator
# of tuples, which we can unpack into keys and values. Items are added to a dictionary by assigning to the key.
# Dictionaries don’t have an append method.

# From Python 3.7 onwards, dictionaries preserve the insertion order. CPython 3.6 also preserves dictionary ordering,
# but that's a feature of that particular implementation. Preserving the order didn't become a language feature until
# Python 3.7.

# We can change values in a dictionary by assigning a new value to the same key.

# There are two ways of removing items from a dictionary: we can use del with the key, but if we try to remove
# something that doesn’t exist, the program will crash.

# The other way is the pop method, which removes a key and returns the value. If the key doesn’t exist, pop will raise
# an error. We can suppress the error by providing a default value, which will be returned when the key isn't present
# in the dictionary.

# Sets also have a pop method. In the case of sets, pop will remove and return an arbitrary item.

# Sets also have remove and discard methods, to remove items from the set. We saw examples of both methods, and looked
# at practical applications for each one.

# After covering the basic operations that can be performed on a dictionary, we put them to practise. This was to
# help you understand the pros and cons of using either a dictionary or a list, e.g. dictionaries may result in
# shorter code, but lists are sorted easily in Python. We used a dictionary techniques to add and remove items in our
# menu program for buying computer parts.

# We learned how two dictionaries can work together, and iterated over the keys of a dictionary to create a new one.
# Although .items() is more commonly used when iterating over a dictionary, we saw that the enumerate function can
# sometimes be useful with a dictionary. We used enumerate to provide numerical "indexes", so we could use dictionary
# items in a menu.

# We further developed our menu program to add more information, and looked at two options for storing them; tuples
# and key/value pairs. Writing the code to retrieve the new values gave you the chance to see why you’d use get
# rather than indexing. This was to help you understand why one data structure works better than another when you
# have a choice.

# We introduced the setdefault method, which returns the value from the dictionary if the key exists. It’s different
# from get because it creates a new entry for the key if the key doesn’t exist. In that case, setdefault assigns a
# default value for the key, and returns that default value.

# We gave some simple examples to show the behaviour of dict methods that you haven’t used yet, e.g. fromkeys(),
# update(), and values(). We then examined the differences between shallow and deep copies.

# A shallow copy copies the references to object. That means the copy will refer to the same objects as the original.
# If you copy an object that contains a list, for example, the copy and the original both refer to the same list.

# A deep copy will create a copy of all contained objects.

# We implemented a simple dictionary using a hash table. This allowed us to see how hashes are used, and how they
# provide very fast access to the values in a dictionary.

# Hash functions are also used in security, but secure hashes are a complex topic, and we only touched on them in
# this section.

# To emphasize the point that you shouldn't attempt to deal with security yourself, we looked at list of data
# breaches on Wikipedia. The list includes some really big names. If large companies, with plenty of money and
# resources, sometimes get security wrong, you can see that it's not something to do with yourself until you've really
# studied computer security.

# Python’s hashlib module implements a common interface to secure algorithms, and we looked at hashing data to verify
# that it wasn't changed. We'll revisit this when we look at storing data in files.

# Python sets work the same as in set theory.
# Sets have no ordering. That's an important point, and is part of the definition of a set.

# We introduced the basic set operations:
# set membership: We test for membership using in.
# set union: We form a union using set.union() or the | operator.
# set intersection: You can produce the intersection of 2 (or more) sets using the set.intersection() method, or the
# & operator.
# set difference: Set difference uses the subtraction operator -. You can also use the set.difference() method.
# symmetric difference: The opposite of intersection. The method is set.symmetric_difference(), or you can use
# the ^ operator.

# Python has 2 ways to perform each operation: a method and an operator. We used the method and the operator
# in each example.

# We used Python sets to solve some common programming problems, and gave examples of when you might use each of
# those operations in practice.

# Because sets are unordered, we can’t index or slice them. However, they are more efficient than lists or tuples
# when checking if an item is present – especially with large amounts of data.

# Besides testing for membership, we can add items to a set, use a set to remove duplicates from data, and delete
# items using remove or discard.

# We saw how the pop() method for sets differs from lists and dictionaries. Because sets have no ordering,
# pop() removes and returns arbitrary items from the set.

# Sets also have methods that can mutate the set. Once again, we used both the methods and the operators in the
# examples:
# update() or |= updates a set by adding the elements from another set (or sets). The result is the union
# of all the sets.
# intersection_update() or &= creates the intersection of the sets.
# difference_update() or -= updates the set to hold the difference.
# symmetric_difference_update() or ^= updates the set so that it contains the symmetric difference.

# We finished the discussion of sets by looking at subsets and supersets.
# Python has both an operator and a method for testing for subsets and supersets.
# If you want to check for a proper subset, or a proper superset, you have to use the operator: < or > respectively.

# We saw practical examples of checking for subsets and supersets.
# Sets are a powerful tool, and can result in significantly less code for many applications.
