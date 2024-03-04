def fibonacci(n):
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result
    # A function may have more than 1 return statement


for i in range(0):
    print(i, fibonacci(i))

# The 'for i in range(0):', loop is not executing any iterations because the range is specified as range(0),
# which creates an empty sequence. As a result, the loop doesn't run, and the print statement inside the loop is
# never executed.

# If you use 'for i in range(-1):', it creates an empty sequence as well. The range(-1) generates an empty sequence
# because it starts from 0 and goes up to, but does not include, the specified endpoint. Since -1 is not a valid
# endpoint, the result is an empty sequence.
