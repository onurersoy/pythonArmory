import json

languages = [
    ['ABC', 1987],
    ['Algol 68', 1968],
    ['APL', 1962],
    ['C', 1973],
    ['Haskell', 1990],
    ['Lisp', 1958],
    ['Modula-2', 1977],
    ['Perl', 1987],
]
# This is deserialized^^

# To serialize Python values to a file, we open a text file for writing, then use the 'json.dump' function.
# The dump function serializes the data we give it, and writes the result to the file.

# TO WRITE:
with open('test.json', 'w', encoding='utf-8') as testfile:
    json.dump(languages, testfile)
    # This is serialized^^
# The contents look exactly like a Python list, containing other lists. That's because Python uses square brackets
# for lists, and JSON uses square brackets for its arrays. JSON isn't specific to Python, this data just happens to
# look very similar to the Python data that we serialized.

# TO READ:
with open('test.json', 'r', encoding='utf-8') as testfile:
    data = json.load(testfile)
print(data)
print(data[2])  # Just to confirm that we are dealing with a list here, and not a string =)
# So we serialized our list to a file, then read it back in again.

# Dealing with a nested structure like this one^^ is easy.
# The json module handles it well, and we retain our original structure.
# Sometimes, you may be dealing with objects that can't be serialized and deserialized so reliably. We'll check
# that in the next section.
