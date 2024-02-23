a = b = c = d = e = f = 12
print(c)

x, y, z = 1, 2, 76  # Those 3 values look suspiciously like a tuple because they already are!
print(x)
print(y)
print(z)
# This is called unpacking a tuple^^

print("Unpacking a tuple")
data = 1, 2, 76  # Data represents a tuple
x, y, z = data
print(x)  # 1
print(y)  # 2
print(z)  # 76

print("Unpacking a list")
data_list = [12, 13, 14]  # It's a list
p, q, r = data_list
print(p)  # 12
print(q)  # 13
print(r)  # 14
# It works for lists too!
# We can unpack the values from any sequence type but since lists are immutable, if something changes in the list,
# your code will break:

data_list2 = [12, 13, 14]
data_list2.append(15)

p, q, r = data_list
print(p)
print(q)
print(r)
# It will result with "Value Error: too many values to unpack (expected 3)".
# Since tuples are immutable, you wouldn't get this error if it was a tuple.
# You can unpack values from a list, as long as you're sure that the size of the list won't be changed.

# Another advantage of tuples, is that you can always unpack them successfully.
# Because a tuple can't be changed, you always know how many items there are to unpack.
# That's why this is described as 'unpacking a tuple', even though you can unpack any sequence type.
