# So it's actually very common to have an if-clause inside a for loop, and we can do that with comprehensions as well.

menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
print(meals)

meals = [meal for meal in menu if 'spam' not in meal]
print(meals)
# Conditional comprehensions: expression + iteration + filter(s)
