available_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi cable", "dvd drive", "type-c cable"]

# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)

current_choice = "-"
computer_parts = []

available_parts.sort()  # So we can find what we are looking for more easily

while current_choice != '0':
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print("\t{0}: {1}".format(number + 1, part))
        print("\t0: to finish\n")

    current_choice = input()

print(computer_parts)
