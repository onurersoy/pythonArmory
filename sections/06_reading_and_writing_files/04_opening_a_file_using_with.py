with open('Jabberwocky.txt', 'r') as jabber:
    for line in jabber:
        print(line.rstrip())
# Opening the files this way is preferred because the files will be automatically closed when the loop terminates!
