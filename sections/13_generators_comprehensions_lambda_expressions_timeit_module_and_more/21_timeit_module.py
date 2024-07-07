import timeit
# The timeit module in Python is used to measure the execution time of small code snippets. It provides a simple way
# to time how long it takes for a piece of code to run, which is especially useful for performance testing and
# optimisation.

# OK, so we imported 'timeit' module. Right, so at this point we've now got a choice; and which one you choose to do is
# entirely up to you. Now we can either turn our three sections of code into functions or we can wrap them in quotes to
# turn them into strings. Let's proceed with the 2nd option...

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

print("nested for loops")
print("----------------")
nested_loop = """\
for loc in sorted(locations):
    exits_to_destination_1 = []
    for xit in exits:
        if loc in exits[xit].values():
            exits_to_destination_1.append((xit, locations[xit]))
    print("Locations leading to {}".format(loc), end='\t')
    print(exits_to_destination_1)
"""

print()

print("List comprehension inside a for loop")
print("------------------------------------")
loop_comp = """\
for loc in sorted(locations):
    exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
    print("Locations leading to {}".format(loc), end='\t')
    print(exits_to_destination_2)
"""
print()

print("nested comprehension")
print("--------------------")
nested_comp = """\
exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
                          for loc in sorted(locations)]

for index, loc in enumerate(exits_to_destination_3):
    print("Locations leading to {}".format(index), end='\t')
    print(loc)
"""

result_1 = timeit.timeit(nested_loop, globals=globals(), number=1000)
# Time to call the globals function^^: 'globals()'.
# So our code snippet will now execute in our global namespace, which means that everything defined in our module will
# be available to the snippet. Now, that could well be overkill, for testing a small snippet of code, but it can be
# useful if the environment is too complex to set up in a small block of code.

# About the 'number=1000' part, please refer to the document of 'timeit' module. Its default value is 1m, and it's
# perfectly fine to leave it that way, but for this time, we set it to 1000, so it can be completed faster.

print(f"Nested loop\t{result_1}")

result_2 = timeit.timeit(nested_loop)
result_3 = timeit.timeit(nested_loop)
