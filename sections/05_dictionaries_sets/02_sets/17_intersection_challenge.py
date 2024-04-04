text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.
words = text.split()
print(words)

# 1st approach:
intersection = prepositions.intersection(set(words))  # << You could directly pass the list too since it's the
# intersection method, not operator.
print(intersection)
intersection2 = prepositions.intersection(words)
print(intersection2)

# 2nd approach:
intersection3 = prepositions & set(words)  # << We had to convert from list to set since it's the operator version.
print(intersection3)
