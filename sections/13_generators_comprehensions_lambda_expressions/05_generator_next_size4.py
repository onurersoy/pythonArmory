import sys


# NEXT:::
# So a generator works like an iterator, and what we can do is, we can actually use 'next' to get the next value instead
# of using it in a loop, and obviously, we used it in a loop in the '03_generator_yield_size2.py' to append the items
# to a list.
def my_range(n: int):
    start = 0
    while start < n+1:
        yield start
        start += 1


big_range = my_range(10)
print(next(big_range))  # 'next' is called here, and it gets the next value from the generator!
print(f"The size of big_range is: {sys.getsizeof(big_range)}")

big_list = []
for value in big_range:
    big_list.append(value)
print(f"The size of big_list is: {sys.getsizeof(big_list)}")

print(big_range)
print(big_list)

print("looping again or not?:")
for i in big_range:
    print(f"i is {i}")
    # Notice that there is nothing to show! The program did not print anything! So iterating over and calling the
    # next value is okay, but if you intend using it again in a for loop, then you should use the my_range() method we
    # created.

print("Trying again:")
for i in my_range(10):
    print(f"i is {i}")
# Instead of our function, we could use built in 'range' function too; range class behaves like an iterable. In
# other words, it's reset each time it's used, which wasn't the case when you used a variable that actually called the
# function that we actually wrote (calling the same function with another variable would work tho, like 'big_range2').
