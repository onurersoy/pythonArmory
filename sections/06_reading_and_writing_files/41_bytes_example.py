# One way to create a 'bytes' object is to pass an iterable – such as a list or tuple – to the bytes function.
# Let's start with a tuple:
equation = bytes((207, 128, 114, 194, 178))
# We can use any iterable, as long as it produces integer values in the range 0 to 255^
# If you remember, from the Lists and tuples section, this is one of the times when a tuple must be enclosed in
# parentheses^
print(equation)
# Bytes and bytearray objects are often used to process Unicode data. Because of that, Python allows you to use a
# string-like syntax when creating a bytes object.
print(type(equation))
print(len(equation))

# Let's comment out line 3, and bind equation to a literal bytes object instead (I will use 'equation2' instead).
equation2 = b'\xcf\x80r\xc2\xb2'  # << This is actually the outcome of line 7
# The value we're binding equation to looks a bit like a string. It's a bytes literal, and Python lets you create a
# literal bytes object in this way.
# The letter b before the string makes it a bytes object, rather than a string.
print(equation2)
# But how did we know that line 3 would produce the values that we had in the original line 3?
for b in equation2:
    print(b, end=', ')
print()
# It might seem strange that Python allows an array of bytes to be defined in the same way as a string, but it makes
# sense when you consider what happens when you read binary data from a Unicode text file. If you open a text file in
# binary mode, you'll read an array of bytes, rather than a string. You can then decode that array, to get a string.
# Let's decode our equation bytes object:
print(equation2.decode('utf-8'))
# So when you read Unicode data as a stream of bytes, you get something like we've got on line 14 & 18. To produce
# a string from those bytes, we decode the string using a suitable encoding. In this case, we specified UTF-8 as the
# encoding (line 27).
