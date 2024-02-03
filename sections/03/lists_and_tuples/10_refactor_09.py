available_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi cable"]
current_choice = "-"
computer_parts = []

while current_choice != '0':
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        computer_parts.append(available_parts[int(current_choice) - 1])
    else:
        print("Please add options from the list below:")
        for part in available_parts:
            print("\t" + str(available_parts.index(part) + 1) + ": " + part)
            # print("\t{0}: {1}".format(available_parts.index(part) + 1, part))
        print("\t0: to finish\n")

    current_choice = input()

print(computer_parts)

# NOTE!: If the list was sorted, we could use a binary search. With us using 'index', Python has to check each item.
# If there are hundreds or thousands of items, finding the index positions will take a while.
# Python provides a much more efficient way of doing it > 'ENUMERATE' Function
# Enumerate returns each item, with its index position (the 1st value is the index position, the 2nd value is the item).
