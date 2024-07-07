import timeit
import functools


# It takes a function and a sequence, then reduces the sequence to a single value by repeatedly calling the function.
def calc_values(x, y: int):
    return x + y


numbers = [2, 3, 5, 8, 13]

reduced_value = functools.reduce(calc_values, numbers)
print(reduced_value)

# We actually have 'sum' function which can get the same result for us here:
print(sum(numbers))
