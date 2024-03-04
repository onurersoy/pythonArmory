# 'Function annotations' make it clearer what kinds of values your functions can accept, and what they return:
def is_palindrome(string: str) -> bool:
    # backwards = string[::-1]
    # return backwards == string # If the evaluation is correct, the function will return 'True', else 'False'
    return string[::-1].casefold() == string.casefold()


def fibonacci(n: int) -> int:
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


def multiply(x: float, y: float) -> float:
    result = x * y
    return result

# You can search about 'type hints' as it's not included on this py file.
