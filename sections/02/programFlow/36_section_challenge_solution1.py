options = ["1. Learn Python", "2. Learn Java", "3. Go swimming", "4. Have dinner", "5. Go to bed", "0. Exit"]


def my_print_statement():
    print("Please choose your option from the list below:\n\n\t{0}\n\t{1}\n\t{2}\n\t{3}\n\t{4}\n\t{5}\n"
          .format(options[0], options[1], options[2], options[3], options[4], options[5]))


my_print_statement()
number = int(input("Enter the selected item number:\n"))

while number != 0:
    if number in range(1, 6):
        print(options[int(number) - 1])
        break
    else:
        print()
        my_print_statement()
        number = input("Enter the selected item number:\n")
