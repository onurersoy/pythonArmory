from data import people, plants_list

# people = []
if all([person[1] for person in people]):
    print("Sending email")
else:
    print("User must edit the list of recipients")
# So as you can see, using all is much simpler than iterating over the list, checking each email address. Another
# advantage of all, and any too, for that matter, is that they short-circuit the evaluation of the iterable. As soon as
# the result is known, they stop checking any more values. In the case of all, it can return false as soon as the false
# value is found. In the case of any, it can return true as soon as a true value is found.

# Remember that the code will fail if the list is empty, and we can see that by setting it to empty before using it^^

# Refactoring so it won't fail if the list is empty:::
people = []
if bool(people) and all([person[1] for person in people]):
    print("Sending email")
else:
    print("User must edit the list of recipients")

if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This pack contains grass")
else:
    print("No grasses in this pack")
