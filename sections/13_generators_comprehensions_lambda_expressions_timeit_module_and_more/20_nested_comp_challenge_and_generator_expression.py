# In an early video, we used a for loop to print the 'times' tables, for values from 1 to 10.
# That was a nested loop, which appears below.
#
# The challenge is to use a nested comprehension, to produce the same values.
# You can iterate over the list, to produce the same output as the for loop, or just print out the list.

for i in range(1, 11):
    for j in range(1, 11):
        print(i, i * j)

times = [(i, i * j) for i in range(1, 11) for j in range(1, 11)]
print(times)

for x, y in [(i, i * j) for i in range(1, 11) for j in range(1, 11)]:
    print(x, y)

times2 = [[(i, i * j) for i in range(1, 11)] for j in range(1, 11)]
print(times2)

# Generator Expression:::
# Now if you intend to use the list again, then a list comprehension does make sense. And in our original solution, we
# could use the 'times' list as often as necessary in the code. Now if you just want to iterate over the list as we're
# doing here, then a generator expression is probably more suitable than a list comprehension. Now generator expressions
# are very similar to write. We just replace the square brackets with parentheses.
for x, y in ((i, i * j) for i in range(1, 11) for j in range(1, 11)):
    print(x, y)  # You can see we've got the same output there. But the difference here with this code is that it's a
    # generator expression, and it isn't creating the entire list in memory. Now just like generators, generator
    # expressions calculate the values as they're requested. The only value that exists is the one that's just been
    # returned.

# Now bear that in mind and consider using a generator expression rather than a list comprehension, if you're not going
# to be using the list more than once.
