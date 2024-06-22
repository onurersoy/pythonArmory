import sys


def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start
        start += 1

_ = input("line 12")
# So we're using an underscore; using that as a variable name in here because that's a Python convention, and indicates
# that we're not interested in the value of the variable.

# big_range = range(5)
big_range = my_range(5)
_ = input("line 15")

print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containing all the values in big_range
big_list = []

_ = input("line 22")
for val in big_range:
    _ = input("line 24 - inside loop")
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)
