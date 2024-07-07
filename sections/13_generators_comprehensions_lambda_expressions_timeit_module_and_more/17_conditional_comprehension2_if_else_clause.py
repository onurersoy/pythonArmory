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

meals = [meal for meal in menu if 'spam' not in meal]
# You CANNOT use an else-clause in an expression, you can only use an if-clause to filter your expression, that's all!
print(meals)


# You can do like these tho:
meals2 = [meal for meal in menu if 'spam' not in meal if "chicken" not in meal]
print(meals2)

meals3 = [meal for meal in menu if 'spam' not in meal and "chicken" not in meal]
print(meals3)
# Notice the above two are actually the same!


fussy_meals = [meal for meal in menu if "spam" in meal or "eggs" in meal if not ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)

fussy_meals = [meal for meal in menu if ("spam" in meal or "eggs" in meal) and not ("bacon" in meal and "sausage" in
                                                                                    meal)]
print(fussy_meals)
# Notice the above two are actually the same!
