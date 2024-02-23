# Function signature means the definition of a function.
# That includes the function's name, and the parameters that it defines.

name = "Tim"
age = 10

print(name, age, "Python", 2020)
print(name, age, "Python", 2020, sep=", ")

################################################

menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=" ")  # In default, end argument takes '\n' as a default value
    print()  # Otherwise all the 'meals' shown in one line
