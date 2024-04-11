jabber = open('Jabberwocky.txt', 'r')
# 'r' = Read (it's the default behaviour)

# To open a file, we use the 'open' function: This isn't the cleanest way to open a file, in Python.
# PEP 343 introduced the 'with' statement for working with things like files. The with statement was added to the
# language in Python 2.5, and we'll be opening all our files using with, once we've seen what it does. At the moment,
# we need to understand some of the basics of working with files.

# If we start with 'with', we might miss out on the concept of closing a file when you've finished with it. So for now,
# don't take this as the best way to open a file – think of it as a way to understand how files work.

# Now we can iterate over:
for line in jabber:
    # print(line, end='')  # << "end=''" so that it won't put a new line after each line, causing an empty line after
    # each new line of our poet.
    print(line.strip())  # << The other way is to 'strip' off the newline from each line of text that we read.
    # print(len(line))

jabber.close()  # << Importantly, we have to close the file when we're finished. If you don't close a file when you're
# finished with it, you can get problems.
# Another consequence of failing to close a file, when writing data to it, is that data might be lost. So it's very
# important to close every file that you open. Python makes this easy as it can close files automatically for us.

# Whitespace is any character that represents horizontal or vertical spacing.
# Whitespace characters aren't visible as characters, but they do space things out. Examples of whitespace characters
# in programming are:
# space, tab, newline.

# Remember that strings are immutable.
# 'str.strip()' won't modify the string. Remember to bind a variable to the result if you want to use the stripped
# string, like below:
stripped = str.strip("Jack")
