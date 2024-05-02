# Built-in data structures that Python provides.
# Bytearray is a mutable version of bytes. 'Bytes' is immutable.
# In the documentation, both types are referred to as bytes-like objects.

# Array:
# 1. It's a sequence of numbers. It's similar to a list - as long as you only put numerical values into the list.
# 2. Python does have an array module in the standard libraries, but it's often more convenient to just use a list.
# 3. Working with arrays is similar to working with lists, and they are indexed in the same way.
# 4. Unlike lists (which are intended to be homogenous), this is enforced with arrays. You can't mix strings and numbers
# in the same array.
# 5. In fact, you can't mix ints and floats in the same array either. All items in an array must be the same type.

# Bytes:
# 1. The bytes data type is an array of bytes. So it's a sequence that can store values in the range 0 to 255.
# 2. Unlike array, which has to be imported, the bytes type is built into Python.
# 3. Each value in a bytes-like object must be a number between 0 and 255.

# What is a byte?:
# Numbers are stored in a computer as a sequence of zeros and ones. That's because computer memory is built using
# transistors, that can either be on or off. We have 2 states, with off representing 0, and on representing 1. So
# computers work in base 2, or binary. A byte is a sequence of 8 binary digits, which are called bits. 8 bits can
# represent a value from 0 to 255. If all the bits are 0, the value of the byte is 0. If all the bits are 1, the value
# of the byte is 255.
