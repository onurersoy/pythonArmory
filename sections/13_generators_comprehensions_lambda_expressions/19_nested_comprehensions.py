# So it's very common to nest one for loop inside another in programming, and we can do the same thing with
# comprehensions, and that's called nested comprehensions.
burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans", "spam"]

meals = [(burger, topping) for burger in burgers for topping in toppings]
print(meals)

for meals in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meals)

print("*" * 20)

# The equivalent for loop:
for burger in burgers:
    for topping in toppings:
        print((burger, topping))

# Now if you're going to iterate over a list, and don't intend to use it again, then seriously consider using a
# generator expression instead!

# Let's continue...
for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(nested_meals)

print("*" * 20)

for nested_meals in [[(burger, topping) for topping in toppings] for burger in burgers]:
    print(nested_meals)
