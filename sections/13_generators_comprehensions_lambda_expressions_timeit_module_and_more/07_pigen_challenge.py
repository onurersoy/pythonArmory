# Create a generator to return an infinite sequence of odd numbers, starting at 1. Print the first 100 numbers to check.
# Note that this is just for testing. We are going to need far more than 100 numbers in a real life scenario, and don't
# know in advance how many, so that's why we're creating our own generator, instead of just using 'range' class.

def oddnumbers():
    n = 1
    while True:
        yield n
        n += 2


# Test code:
# odds = oddnumbers()
# for i in range(100):
#     print(next(odds))

# Remember that a generator will continue from where it left off after yielding a value.

def pi_series():
    odds = oddnumbers()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


approx_pi = pi_series()
for x in range(10000000):
    print(next(approx_pi))
