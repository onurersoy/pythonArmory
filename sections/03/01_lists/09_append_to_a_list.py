current_choice = "-"
computer_parts = []

while current_choice != '0':
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        if current_choice == '1':
            computer_parts.append("computer")
        elif current_choice == '2':
            computer_parts.append("monitor")
        elif current_choice == '3':
            computer_parts.append("keyboard")
        elif current_choice == '4':
            computer_parts.append("mouse")
        elif current_choice == '5':
            computer_parts.append("mouse mat")
        elif current_choice == '6':
            computer_parts.append("hdmi cable")
    else:
        print("Please add options from the list below:")
        print("\t1: computer")
        print("\t2: monitor")
        print("\t3: keyboard")
        print("\t4: mouse")
        print("\t5: mouse mat")
        print("\t6: hdmi cable")
        print("\t0: to finish")

    current_choice = input()

print(computer_parts)
