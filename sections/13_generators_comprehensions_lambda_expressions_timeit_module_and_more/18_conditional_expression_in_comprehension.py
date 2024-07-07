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
    else:
        meals.append("a meal was skipped")
print(meals)

# Adapting 'else' logic to conditional comprehensions:
meals = [meal if "spam" not in meal else "a meal skipped" for meal in menu]
# Just in case this isn't clear, what we've done is remove the filter, and we've put the conditional expression in the
# comprehension.
# conditional expressions = expression + iteration

x = 15
expression = "Twelve" if x == 12 else "unknown"
print(expression)

print("*" * 20)

for meal in menu:
    print(meal, "contains sausage" if "sausage" in meal else "contains bacon" if "bacon" in meal else "contains egg")

print("*" * 20)

items = set()
for meal in menu:
    for item in meal:
        items.add(item)
print(items)

for meal in menu:
    for item in items:
        print(f"{meal} contains {item}")

for x in range(1, 31):
    fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
    print(fizzbuzz)
