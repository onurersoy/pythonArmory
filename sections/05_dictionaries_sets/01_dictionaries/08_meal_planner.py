from contents import *


# from contents import pantry, recipes

# def add_shopping_item(data: list, item: str, amount: int) -> None:
#     """Add a tuple containing `item` and `amount` to the `data` list."""
#     data.append((item, amount))

def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """Add a tuple containing `item` and `amount` to the `data` dict."""
    # if item in data:
    # Augmented assignment:

    #     data[item] += amount
    # else:
    #     data[item] = amount

    # Let's improve the above code:
    data[item] = data.setdefault(item, 0) + amount  # This one does the same thing that above code does.
    # PS. `setdefault` method is specific to dictionaries!


# print(pantry)
# print(recipes)

# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
# The above is just a reminder for us as it's the most efficient way to achieve what we are aiming here, but before
# understanding the code above, we have to learn about dictionary comprehensions, and we will in the near future.

# For now, let's go like this:
display_dict = {}
for index, key in enumerate(recipes):
    print(index, key)
    # Dictionaries don't have index numbers, they use the keys to index into a dictionary. The enumerate function
    # creates the index numbers for us.
    display_dict[str(index + 1)] = key

# shopping_list = []
shopping_dict = {}

while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)  # So if the item isn't in the pantry at all, we will get a
            # default value of '0', avoiding raising an exception
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy: {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_dict, food_item, quantity_to_buy)
                # If you want, you could use the 'colorama' module, to print the output in different colours.

for things in sorted(shopping_dict):
    print(things)
