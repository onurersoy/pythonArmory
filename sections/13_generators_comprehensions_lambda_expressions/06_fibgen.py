def fibonacci():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current
        # Remember that the part on the right side is getting calculated first, so it acts like this:
        # "previous = current"
        # Then; "current (it's the new 'current') = current + previous"


# This is an infinite generator^^. Using it like this would give us an infinite loop:
# fib_pre = fibonacci()
# for f in fib_pre:
#     print(f)

fib = fibonacci()
for i in range(10):
    print(next(fib))
