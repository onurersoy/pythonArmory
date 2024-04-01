import copy  # << copy module

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

# Performs a shallow copy:
# things = animals.copy()

# Let's perform a deep copy:
things = copy.deepcopy(animals)

print(things["teddy"])  # '["cuddly", "stuffed"]'
print(id(things["teddy"]))
print(animals["teddy"])  # '["cuddly", "stuffed"]'
print(id(animals["teddy"]))
# Notice that the 'ids' are different now.

print()

things["teddy"].append("toy")
print(things["teddy"])  # It was and still is '["cuddly", "stuffed", "toy"]' on shallow copy
print(animals["teddy"])  # It was '["cuddly", "stuffed", "toy"]' on shallow copy
# It is now '["cuddly", "stuffed"]'on deep copy!

# PS. Each dictionary now contains its own copy of the lists!
