letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
# PS. '-1' is the step value, which means you're moving from right to left. It won't be ignoring any items.
# Slicing Idioms^^
print(backwards)

print(letters[16:13:-1])
print(letters[4::-1])
print(letters[25:17:-1])
print(letters[:-9:-1])

print(letters[-4:])
print(letters[-1:])
# PS. If you don't use '-1' as step, it's going from left to right. Depends on using '-1' as step or not, the 1st
# and the last item are changing (f.e. right to left).
print(letters[1:])
