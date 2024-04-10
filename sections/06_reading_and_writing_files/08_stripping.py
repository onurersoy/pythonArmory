# The 'strip', 'lstrip', and 'rstrip' methods are commonly used when processing text files. We've already
# seen how to strip whitespace, including the newline, from the end of a line.

# strip(chars): Removes leading and trailing characters specified in the 'chars' argument. If no argument is provided,
# it removes whitespace characters (spaces, tabs, newlines). If an argument is provided, it remes the specified argument
# and also the whitespace characters.

filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)

chars = "'"
no_apostrophe = first.strip(chars)
print(no_apostrophe)

chars2 = "' Twasebv"
no_apostrophe2 = first.strip(chars2)
print(no_apostrophe2)

for character in first:
    if character in chars2:
        print(f'removing "{character}"')
    else:
        break

print('*' * 80)

for character in first[::-1]:  # process backwards
    if character in chars2:
        print(f'removing "{character}"')
    else:
        break
