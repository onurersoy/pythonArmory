# We've left it till last, because you probably won't use it very often. We'll see what it does, then I'll
# explain why it's not as useful as 'read' and 'readlines'.

with open('Jabberwocky.txt') as jabber:
    while True:
        line = jabber.readline().rstrip()  # It brings lines 'line-by-line'; similar to iterating over the file object.
        # The outcome is a string.
        print(line)
        if 'jubjub' in line.casefold():
            break
        # Here, we read the file line-by-line, and break out of the loop when we find something we're looking for.
        # Run the program and the program terminates when it finds the line containing "Jubjub".

        # That's one use for readline. It reads one line of the file at a time.

        # The reason you might not use it very often is that we can get the same result by just iterating over the
        # file object – which is what we did when we first looked at reading from a text file ('03_reading_poem.py').

print('*' * 80)

# Here's the equivalent code:
with open('Jabberwocky.txt') as jabber:
    for line in jabber:
        print(line.rstrip())
        if 'jubjub' in line.casefold():
            break

# PS. We stopped putting 'r' to these lines of code on 'readlines()', 'read()' and 'readline()' examples:
# >> 'with open('Jabberwocky.txt', 'r') as jabber:'
# It's because it's the default behavior; which is opening a file to read.
