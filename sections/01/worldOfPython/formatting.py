# 9

for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    # Let's format the string so all the numbers can line up with the below row:
    # RIGHT-ALIGN:
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))
    # print("No. {0:<2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3)) # Same with the above line^^

print()

for i in range(1, 13):
    # LEFT-ALIGN:
    print("No. {0:>2} squared is {1:>3} and cubed is {2:>4}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    # CENTER-ALIGN:
    print("No. {0:^2} squared is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

# Format specifier controls the width and precision of the field for the floating-point number, and how it's
# displayed in the string.
print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))
