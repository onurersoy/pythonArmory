# Let's make the code (02.23) better by using 'else' in a 'while' loop:

available_exists = ["north", "south", "east", "west"]

chosen_exist = ""
while chosen_exist not in available_exists:
    chosen_exist = input("Please choose a direction: ")
else:
    print("Aren't you glad you got out of there")
