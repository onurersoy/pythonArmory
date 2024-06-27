import timeit

# Now let's use the 'function' approach.

setup = """\
gc.enable()
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
"""

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


def nested_loop():
    result = []
    for loc in sorted(locations):
        exits_to_destination_1 = []
        for xit in exits:
            if loc in exits[xit].values():
                exits_to_destination_1.append((xit, locations[xit]))
        result.append(exits_to_destination_1)
        return result


def loop_comp():
    result = []
    for loc in sorted(locations):
        exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
        result.append(exits_to_destination_2)
    return result


def nested_comp():
    exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
                              for loc in sorted(locations)]
    return exits_to_destination_3


def nested_gen():
    exits_to_destination_4 = ([(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
                              for loc in sorted(locations))
    return exits_to_destination_4


print(nested_loop())
print(loop_comp())
print(nested_comp())

result_1 = timeit.timeit(nested_loop, setup, number=10000)
result_2 = timeit.timeit(loop_comp, setup, number=10000)
result_3 = timeit.timeit(nested_comp, setup, number=10000)
result_4 = timeit.timeit(nested_gen, setup, number=10000)
# Now that's how you can time functions using timeit, rather than wrapping things up in strings. But be aware that it
# will only work with functions that don't take any arguments. If you need to pass arguments to your function, then you
# can't pass the function directly to the timeit function.
print(f"Nested loop\t{result_1}")
print(f"Loop comprehension\t{result_2}")
print(f"Nested comprehension\t{result_3}")
print(f"Nested gen\t{result_4}")
# Notice that there's a huge difference, compared to the other three. The nested_gen function looks to be over 10
# times faster.
# Once again, that's not really surprising. The generator isn't spending time building up the lists - it's just going to
# return each one when we iterate over it. So before you rush off and decide that you'll use generator expressions for
# everything, it is important to realize that you don't get something for nothing. So creating the generator is a lot
# faster than using loops or list comprehensions to build up the lists, but we'll pay for it when we come to iterate
# over the generator.
