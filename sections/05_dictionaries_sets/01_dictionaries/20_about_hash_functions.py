# HOW CAN DICTS FETCH THE VALUES SO FAST?

# Object used as a key on a dict must be hashable.
# An object is hashable if it has a hash value which never changes during its lifetime.
# A hash function is any function that can be used to map data of arbitrary size to fixed-size values.
# The hash function always returns integer values.
# The values returned by a hash function are called hash values, hash codes, digests, or simply hashed.
# The values are used to index a fixed-size table called a hash table. Use of a hash function to index a hash table is
# called hashing or scatter storage addressing.
# Hashes can be used like indexes.
# If you can calculate a hash, and use if to go directly to an entry in a hash table, then accessing the data becomes
# very fast.

# That's why retrieving a value from a dictionary, using its key, is so fast.
# The speed doesn't depend on how many items are in the dictionary, it depends on how fast the hashing function can
# calculate the hash.

# There are many different ways to implement a hash function. There's no single way to write one, and different
# algorithms have their own strengths, weaknesses and applications.

# A hash function produces values that can be used to index a fixed-sized data structure, called a hash table. If the
# hash table can hold 500 items, then the hash function should produce 500 distinct hashes.

# A hash (or hash code) doesn't have to be unique. For example, two different strings can have the same hash. That's
# known as a 'collision'.

# There are several different strategies for handling collisions. One of the simplest, is to dump all keys with the same
# hash into the same 'bucket'. You then compare each item in the bucket with the original key, to see if it exists.

# Because handling collisions is slower than indexing directly into the table, it's important that a hash function
# produces as few collisions as possible.

# The best case is that every key has a unique hash.
