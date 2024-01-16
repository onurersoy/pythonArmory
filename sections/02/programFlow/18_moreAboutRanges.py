# If you do not provide a starting value, it will start from 0 as default to 9 as the finishing value is never-
# -included on a range
for i in range(10):
    print("i is now {}".format(i))

# 0, 2, 4, 6, 8
for i in range(0, 10, 2):
    print("i is now {}".format(i))

# 10, 8, 6, 4, 2
for i in range(10, 0, -2):
    print("i is now {}".format(i))

age = int(input("How old are you? "))
# if 16 <= age <= 65:
if age in range(16, 66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")
