d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "iv": "four",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

v = d.values()
print(v)


d[10] = "ten"
print(v)

# Dictionary view objects:
# The objects returned by 'dict.keys()', 'dict.values()', and 'dict.items()' are view objects. They provide a dynamic
# view on the dictionary's entries, which means that when the dictionary changes, the view reflects these changes.

print("four" in v)  # True
print("eleven" in v)  # False

keys = list(d.keys())
values = list(v)  # list(d.values())
if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with the key {key}")

print()

for key, value in d.items():
    if values == "four":
        print(f"{d[key]} was found with the key {key}")
