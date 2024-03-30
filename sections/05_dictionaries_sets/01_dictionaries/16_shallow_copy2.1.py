lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]

animals = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}

things = animals.copy()  # << Shallow copy

teddy_list.append("toy")
print(things["teddy"])  # '["cuddly", "stuffed", "toy"]'
print(animals["teddy"])  # '["cuddly", "stuffed", "toy"]'
# It's because they both have the same references of values (because '.copy' method is copying the values of 'animals'
# too which is references to some lists), which is f.e 'teddy_list'.
# The value of the "lion" key in 'animals', and the value of the "lion" key in 'things', both refer to the same list.
# We are performing a 'shallow copy' here. The list isn't copied.
# A shallow copy copies references. It doesn't make a copy of the things that are being referred to.

# If the values are immutable, such as strings or ints, then we don't really care about references being copied.
# If you can't mutate a value, then none of this really matters. Where it becomes important to understand all this,
# is when the values refer to mutable objects. As we saw, adding "toy" to the "teddy" value in 'things, resulted
# in "toy" appearing in the "teddy" value for 'animals' too (Check '16_shallow_copy2.1.py').
