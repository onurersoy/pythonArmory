# A tuple is a mathematical name for an ordered set of data
# Being ordered is a requirement for a Python sequence
# In Python, tuples are another sequence type; along with strings, lists and ranges
# Tuples differ from lists because tuples are 'immutable'. That means they can't be changed after they're created,
# just like strings.

t = "a", "b", "c"
print(t)  # Notice that no parentheses on the terminal, so you can tell that it's not a list but tuple
t = ("a", "b", "c")  # This the exact same tuple with the above one so the parentheses are optional but use as best
# practices.

# There are some must-use cases for parentheses on tuples like:
name = "Tim"
age = 10

print(name, age, "Python, 2020")  # print function prints multiple/separate values; it prints 4 different objects here
print((name, age, "Python, 2020"))  # print function prints a tuple here
# So when you use a tuple as an argument to function, you have to use parentheses
# You may find it easier to always enclose your tuples in parentheses to avoid having to remember when they're necessary
