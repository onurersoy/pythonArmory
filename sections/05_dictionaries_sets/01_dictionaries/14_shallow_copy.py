animals = {
    "lion": "scary",
    "elephant": "big",
    "teddy": "cuddly",
}

# things = animals # 'things' is actually another reference of 'animals'.
# animals["teddy"] = "toy"
# print(things["teddy"])  # "toy"

things = animals.copy()  # 'things' is now a new dict by copying 'animals.

animals["teddy"] = "toy"
print(things["teddy"])  # "cuddly"
print(animals["teddy"])  # "toy"
