# Endianness refers to the order that the bytes are stored, in multi-byte numbers.
# Little endian means that the least significant byte appears first. Like writing from right to left.
# Big endian is the other way around - the most significant byte appears first. Like writing from left to right.

# 100 + 20 + 3 = 123 (big endian)
# We would read like 321 if it was in little endian.

# Why do ve have these 2 systems?:
# It's all connected to the underlying architecture of the CPUs. Intel microprocessors use little endian. IBM
# mainframes use big endian. It comes down to the design of the hardware, and che choice that the designers made.

# The internet uses big endian, and you'll sometimes hear that referred to as network order.
