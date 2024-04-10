with open('Jabberwocky.txt', 'r') as jabber:
    lines = jabber.readlines()
    # The 'readlines' method returns a list, containing strings for each line from the file!

print(lines)
print(lines[-1:])  # << to fetch the last line

for line in reversed(lines):
    # To get the lines in a reversed order
    print(line, end='')  # do some processing in reverse order

#  We've read every single line into a list. That works fine for this short "Jabberwocky" file, but what if you're
#  trying to process a file that contains millions of lines? The file might be too big to fit into memory.

# As the documentation says, "it's your problem if the file is twice as large as your machine's memory".
# 'readlines' can be useful when dealing with files that will fit into memory.

# That also applies to the 'read' function. Unlike 'readlines', 'read' doesn't split the lines up. Instead, it returns
# a single string containing all the characters in the file.
