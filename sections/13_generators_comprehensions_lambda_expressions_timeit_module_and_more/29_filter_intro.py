# One of the other functions that Guido van Rossum wanted to remove from the standard library, is filter. So in this
# module, we're going to have a look at what it does and how a comprehension can be used to achieve the same result.

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

for meal in menu:
    if "spam" not in meal:
        print(meal)

print("-" * 40)

meals = [meal for meal in menu if 'spam' not in meal]
print(meals)

print("-" * 40)


# FILTER:::
def not_spam(meal_list: list):
    return "spam" not in meal_list


spamless_meals = list(filter(not_spam, menu))
print(spamless_meals)
