# If you attempt to read a file in Python and get strange results, the first thing to check is the file encoding.
# We've seen a strange result already when we attempted to read the Jabberwocky file. If you're using Linux or a Mac, it
# probably looked fine. But on Windows, you may have had a strange result at the end of the file. To fix that:
with open('Jabberwocky.txt', 'r', encoding='utf-8') as jabber:
    for line in jabber:
        print(line.rstrip())
