import sys


def my_range(n: int):
    start = 0
    while start < n+1:
        yield start
        start += 1
# In a normal function (let's say without 'yield' here), a function finishes after returning the result. The difference
# is that when we use 'yield', the function actually returns the yielded value, then goes into a sort of suspended
# state. So it doesn't just return the value - it keeps track of all its variables and whereabouts in its code, it is.
# So the next time it's called, it wakes up and continues from where it left off.

# So looking at this code on line 18, where the function call is, you might be thinking it only gets called once, but in
# fact it's called each time it's iterated over in the loop on line 23.

# big_range = range(1000)  # << This is a generator
big_range = my_range(1000)
print(f"The size of big_range is: {sys.getsizeof(big_range)}")

# Create a list containing all the values in big_range
big_list = []  # << This is a list
for value in big_range:
    big_list.append(value)
print(f"The size of big_list is: {sys.getsizeof(big_list)}")

print(big_range)
print(big_list)
