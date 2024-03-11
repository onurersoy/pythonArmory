# Recursive function solution:
def factorial(n: int) -> int:
    """
    Return n! (0! is 1).

    Valid for `n` in the range 0 to 998 (inclusive).
    Larger values of `n` will cause a RecursionError.
    """
    if n <= 1:
        return 1

    return n * factorial(n - 1)


for i in range(36):
    print(i, factorial(i))

# While recursive solutions can be elegant and easy to understand, they may not be the most efficient for certain
# cases, especially when dealing with large values. The recursive solution for factorial has a time complexity of O(
# n) because it makes n recursive calls, but it also has a space complexity of O(n) due to the recursive call stack.
# This can lead to a stack overflow for large values of n, and it's not the most efficient way to compute factorials.

# For large values of n, using an iterative approach or optimizing the recursive solution through techniques like
# memoization or dynamic programming is more efficient. Iterative approach (check '19_factorial_challenge1.py')
# avoids the risk of a stack overflow and is generally more efficient for large values. Additionally, Python has a
# built-in math.factorial function that is implemented in C and optimized for performance!
#
# In summary, while recursion is a powerful tool, it's essential to consider its limitations and potential
# performance issues for certain cases. For calculating factorials of large values, an iterative solution or using
# specialized functions is usually a better choice.
