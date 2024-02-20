available_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi cable"]
current_choice = "-"
computer_parts = []

while current_choice != '0':
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        computer_parts.append(available_parts[int(current_choice) - 1])
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print("\t{0}: {1}".format(number + 1, part))
        print("\t0: to finish\n")

        # We can use enumerate function with all iterables; and all sequences are iterable.

    current_choice = input()

print(computer_parts)
