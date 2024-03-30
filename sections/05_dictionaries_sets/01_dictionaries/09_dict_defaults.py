from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
# If `chicken` exists, then it returns its value, otherwise it returns its default value, which is `0` and adds this
# record to our dictionary!
print(f"chicken: {chicken_quantity}")

beans_quantity = pantry.setdefault("beans", 0)
# 'beans' don't exist in the pantry!
# But this method also makes 'beans' included in our dictionary!
print(f"beans: {beans_quantity}")

ketchup_quantity = pantry.get("ketchup", 0)
# get method here with default value 0 only returns the default value (because it is not in our dict), it doesn't
# add it to the dictionary.
print(f"ketchup: {ketchup_quantity}")

# The 'default' value doesn't have to a number, we can store anything on a dict:
z_quantity = pantry.setdefault("zucchini", "eight")
print(f"zucchini: {z_quantity}")

print()
print("'pantry' not contains:   ")

for key, value in sorted(pantry.items()):
    print(key, value)

# PS. Also check '08_meal_planner' for a better alternative to augmented assignment!
