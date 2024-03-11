# *args

numbers = (0, 1, 2, 3, 4, 5)

print(numbers)
print(numbers, sep=";")

print(*numbers)  # *numbers = a tuple to be unpacked
print(0, 1, 2, 3, 4, 5)

print(*numbers, sep=";")
print(0, 1, 2, 3, 4, 5, sep=";")


def test_star(*args):  # Python here packs them for us :: *args represents an unpacked tuple here
    # You can pass zero, 1 or more than 1 parameter^^
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)  # already an unpacked tuple

print()  # print function here runs with its default parameter, which is a 'new line'
test_star()
