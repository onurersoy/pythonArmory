# Python has comprehensions for lists, sets, and dicts. And it also has generator expressions which are very similar
# to write.

print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

squares = [number ** 2 for number in numbers]  # << list comprehension
squares_set = {number ** 2 for number in numbers}  # << set comprehension
# Everything about list comprehensions also applies for set comprehensions. The only difference is one produces a list,
# while the other one produces a set.

print(squares)
# It's almost exactly the same thing with '10_list_for_loop.py'.

# Now, this list comprehension is in 2 parts:
# 'number ** 2'     >> Expression that we want to return.
# 'for number in numbers'   >> Iteration over a sequence. It's identical to the for part of our for loop in
# '10_list_for_loop.py'.
# We can use anything that can be iterated over - a string, for example, or a generator such as a range and such.
squares2 = [number ** 2 for number in range(1, 7)]
print(squares2)
