# Continue Statement
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# Let's iterate over the list:
for item in shopping_list:
    if item != "spam":
        print("Buy " + item)

print("-" * 10)

# Now let's try another approach:
# CONTINUE STATEMENT:
for item in shopping_list:
    if item == "spam":
        continue
    print("Buy " + item)

print("-" * 10)

# Another approach:
for item in shopping_list:
    if not item == "spam":
        print("Buy " + item)
