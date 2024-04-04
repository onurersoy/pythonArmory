from primes_and_squares import  squares_generator, primes_generator

# Intersection = Kesişim
# The intersection of 2 sets is the set of elements that are present in both sets.

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print(evens)
print(odds)

primes = set(primes_generator(100))
print(primes)
squares = set(squares_generator(100))
print(squares)

print(odds.intersection(squares))  # << intersection method
# It produces a new set, containing those elements that are in both the sets.
print(evens & squares)    # << intersection operator
# It produces a new set, containing those elements that are in both the sets.

# The intersection method is more readable than the operator if you're not a mathematician working with set theory.
# It has another advantage – as do all these methods. You can pass an 'iterable' to it, instead of a set.

# Let's pass an iterable to the method:
even_squares = evens.intersection(squares_generator(100))  # Notice that it is equal with '(evens & squares)'.
print(even_squares)
# You can't do that^^ with the operators. They only work when both objects are sets!
