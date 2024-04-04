travel_mode = {"1": "car", "2": "plane"}

items = {
    "can opener",
    "fuel",
    "jumper",
    "knife",
    "matches",
    "razor blades",
    "razor",
    "scissors",
    "shampoo",
    "shaving cream",
    "shirts (3)",
    "shorts",
    "sleeping bag(s)",
    "soap",
    "socks (3 pairs)",
    "stove",
    "tent",
    "mug",
    "toothbrush",
    "toothpaste",
    "towel",
    "underwear (3 pairs)",
    "water carrier",
}

restricted_items = {
    "catapult",
    "fuel",
    "gun",
    "knife",
    "razor blades",
    "scissors",
    "shampoo",
}

print("Please choose your mode of travel:")
for key, value in travel_mode.items():
    print(f"{key}: {value}")

mode = "-"
while mode not in travel_mode:
    mode = input("> ")

if mode == "2":
    # travelling by plane, remove restricted items
    # for restricted_item in restricted_items:
    #     # remove will give an error here
    #     items.discard(restricted_item)
    # items -= restricted_items # << we could use this one too # << I'll use 'difference update', because we want to
    # modify the original items set^^
    items.difference_update(restricted_items)

    # If you find yourself looping over the items in a set, and performing some operation on another set, check out
    # the set operations. They're very efficient and can save you writing loops. Writing less code can mean
    # introducing fewer bugs, which is a good thing.

# print the packing list
print("You need to pack:")
for item in sorted(items):
    print(item)
