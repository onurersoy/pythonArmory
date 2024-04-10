with open('Jabberwocky.txt') as jabber:
    text = jabber.read()

print(text)
# The output looks the same (comparing with 'readlines'), but we've now got a string, rather than a list.
# That becomes obvious when we come to process text.

for character in reversed(text):
    print(character, end='')
