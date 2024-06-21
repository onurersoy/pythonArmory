# There are two types of errors we can get. There are syntax errors and exceptions.
# Now, the thing to remember is if you don't handle an exception in your code when it occurs, then the program
# actually crashes. In summary, it is called an 'unhandled exception' and execution of the program stops.
# Built-in exceptions link: https://docs.python.org/3/library/exceptions.html
def factorial(n):
    # n! can be defined as n * (n-1)!
    """ calcılates n! recursively"""
    if n <= 1:
        return 1
    else:
        print(n / 0)  # Just to raise a zero-division exception. When an exception is raised in a try block, Python
        # checks the except clauses to see if there's one that handles that particular exception.
        n * factorial(n - 1)


try:
    print(factorial(900))
except RecursionError:  # It's a good practice to be explicit about which exceptions you're handling, and you can have
    # several except clauses if you want to.
    # This exception may raise due to lack of memory to calculate the factorial for the given number.
    print("This program cannot calculate factorials that large")
except ZeroDivisionError:
    print("What are you doing dividing by zero???")
# We could combine these exceptions above, check for the next module! (But then we wouldn't be able to do different
# things after each different type of exception, so it all depends on what you need and what you want to achieve.)

print("Program terminating")
