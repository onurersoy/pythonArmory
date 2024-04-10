# removeprefix and removesuffix are added on Python 3.9!

filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)

print('*' * 80)

twas_removed = first.removeprefix("'Twas")
print(twas_removed)
toves_removed = first.removesuffix('toves')
print(toves_removed)

# If you do not use Python 3.9 or a newer version, or you want another way to achieve the same above, you can always
# create your own function to do this:

print('*' * 80)


def removeprefixcustom(string: str, prefix: str) -> str:
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:]  # Return a copy of 'string'.


def removesuffixcustom(string: str, suffix: str) -> str:
    if suffix and string.endswith(suffix):  # suffix='' should not call string[:-0]
        return string[:-len(suffix)]
    else:
        return string[:]  # Return a copy of 'string'.


twas_removed_custom = removeprefixcustom(first, "'Twas")
print(twas_removed_custom)
toves_removed_custom = removesuffixcustom(first, '')
print(toves_removed_custom)

# That's how you can remove a prefix or suffix from a string. As you now, that's not what the 'strip' methods do.
# They remove all from a sequence of characters until a non-matching character is found.
