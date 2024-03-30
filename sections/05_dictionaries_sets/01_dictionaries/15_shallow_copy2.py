animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

things = animals.copy()  # << Shallow copy

print(things["teddy"])  # '["cuddly", "stuffed"]'
print(animals["teddy"])  # '["cuddly", "stuffed"]'

print()

things["teddy"].append("toy")
print(things["teddy"])  # '["cuddly", "stuffed", "toy"]'
print(animals["teddy"])  # '["cuddly", "stuffed", "toy"]' >> How tho?? Check '16_shallow_copy2.1.py'.
