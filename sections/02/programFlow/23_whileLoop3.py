available_exists = ["north", "south", "east", "west"]

chosen_exist = ""
while chosen_exist not in available_exists:
    chosen_exist = input("Please choose a direction: ")
    # We can use CONTINUE & BREAK STATEMENTS just like we use in for loops:
    # PS. String comparisons are always case-sensitive!
    # PS. The 'casefold()' method returns a string where all the characters are lower case
    if chosen_exist.casefold() == "quit":
        print("Game over")
        break

print("Aren't you glad you got out of there")
