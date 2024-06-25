text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]
print(capitals)

words = [word.upper() for word in text.split(' ')]
print(words)

lc_words = text.split(' ')
print(lc_words)

lc_words = [word for word in text.split(' ')]  # << Do not do this!
# Notice that the outcome is exactly the same with line 9, so there is no need to use a comprehension here. It only
# makes your code more complex, and it doesn't specifically solve a problem.
# We still need to see why a comprehension is useful except making 3 lines of code to a single line of code...
