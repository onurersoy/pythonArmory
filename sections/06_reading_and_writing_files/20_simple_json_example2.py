import json

# # Sometimes, you may be dealing with objects that can't be serialized and deserialized so reliably:
languages = [
    ('ABC', 1987),
    ('Algol 68', 1968),
    ('APL', 1962),
    ('C', 1973),
    ('Haskell', 1990),
    ('Lisp', 1958),
    ('Modula-2', 1977),
    ('Perl', 1987),
]
# We changed the list of list on '19_simple_json_example.py' to a list of tuples.

with open('test2.json', 'w', encoding='utf-8') as testfile:
    json.dump(languages, testfile)

# TO READ:
with open('test2.json', 'r', encoding='utf-8') as testfile:
    data = json.load(testfile)
print(data)
print(data[2])
# This time we are serializing a list of tuples, but we get back a list of lists. The JSON format doesn't support
# tuples. That's not surprising; many languages don't even have tuples, so they'd be unable to parse them out of the
# JSON text. Remember that JSON is a format for exchanging data. As long as you can get the data in a form that you
# can work with, in your code, then it's serving its purpose. JSON has to be language independent, otherwise it
# wouldn't be an open standard that can be used with any language. That means it can only support objects that are
# common in all languages.

# Limitations of JSON:
# Use JSON when you want to store data, or transmit it, in a format that other systems can use. JSON isn't suitable for
# storing your program's data if you need to preserve the exact type.
# As we've seen, it can only be used to represent a limited number - 7 - of data types ('pythonArmory [Udemy]' document
# can be checked for further info).
# Those types are usually sufficient when you're only interested in the actual data. They're not suitable when the
# exact type of the object is important. That's rarely the case when transferring JSON, but it is important if you
# want to save data in your program, and get back exactly what you saved later.

# JSON only supports 7 data types ('pythonArmory [Udemy]' document can be checked for further info)
# In particular, there's no support for things like dates. The decoding program needs to know how you've stored your
# dates in strings. There is an international standard for storing dates (google ISO 8601 for details). When including
# dates in your JSON data, we definitely recommend sticking to one of the formats in that standard.
