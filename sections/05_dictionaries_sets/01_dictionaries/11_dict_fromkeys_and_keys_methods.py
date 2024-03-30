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
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

# 1st:
new_dict = dict.fromkeys(pantry_items)
print(new_dict)
# We can change the default value by giving another argument to the method:
new_dict2 = dict.fromkeys(pantry_items, 0)
print(new_dict2)

# 2nd:
keys = d.keys()
print(keys)
# If you see '.keys(), you can tell that you are dealing with a dictionary.

for item in d:
    print(item)
# The above and below code produces the same result. It's better to use the below one, so you can tell what you are
# iterating over.
for item in d.keys():
    print(item)
