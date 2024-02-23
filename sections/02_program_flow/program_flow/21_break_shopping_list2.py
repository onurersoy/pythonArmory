# Break Statement
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None

# BREAK STATEMENT:
for index in range(len(shopping_list)):
    # INFO: len is short for 'lenght'
    if shopping_list[index] == item_to_find:
        found_at = index
        break

# PS. You can iterate in a String, Range or List (Sequence)!
# To make the code above better:
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found.".format(item_to_find))
