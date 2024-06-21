def factorial(n):
    # n! can be defined as n * (n-1)!
    """ calcılates n! recursively"""
    if n <= 1:
        return 1
    else:
        print(n / 0)
        n * factorial(n - 1)


try:
    print(factorial(900))
except (RecursionError, ZeroDivisionError):
    print("This program cannot calculate factorials that large")

print("Program terminating")
