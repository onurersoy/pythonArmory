shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
print(id(another_list))

# There is only 1 list above^^
# So you can bind multiple names to a List

# APPEND FUNCTION:
another_list.append("ice cream")
print(another_list)
print(id(another_list))
