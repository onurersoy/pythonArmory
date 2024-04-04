from primes_and_squares import  squares_generator, primes_generator

# Difference = 'Fark kümesi'
# Use-case: F.e when you want to remove everything that exists in a set, you can avoid having to iterate over the set.
# We do that by using the set difference operation.

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print(evens)
print(odds)

primes = set(primes_generator(100))
print(primes)
squares = set(squares_generator(100))
print(squares)

print()

print(odds.difference(primes))  # << difference method (A/B)
print(odds - primes)  # << difference operator (A/B)

print(primes.difference(odds))  # (B/A)
print(primes - odds)  # (B/A)
