# Remember that Python standard libraries are automatically imported, and you don't have to do anything regarding
# importing.
# Python Built-in Functions: https://docs.python.org/3/library/functions.html#built-in-funcs

print(dir())
# print(dir(__builtins__))
for m in dir(__builtins__):
    print(m)

print()

import shelve
help(shelve)

print()

print(dir())  # Notice that 'shelve' is now added to the list as we imported it (it's not a built-in module)
for obj in dir(shelve.Shelf):
    print(obj)
    if obj[0] != '_':
        print(obj)
