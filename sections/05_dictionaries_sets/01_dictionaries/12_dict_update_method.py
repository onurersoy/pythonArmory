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

d2 = {
    7: "lucky seven",
    10: "ten",
    3: "this is the new three",
}

d.update(d2)
for key, value in d.items():
    print(key, value)

print()

d.update(enumerate(pantry_items))
for key, value in d.items():
    print(key, value)
# The enumerate function creates an iterable of key value pairs as tuples. So take a close look at the behaviour of the
# code above. Since a key in a dict is unique, the first 5 values are getting updated with 'pantry_items'.
