# The same as updating nonlocal variables, try to avoid updating global variables from an inner scope. The inner
# scope might be a function, or it might be a class... Ideally, your code shouldn't modify anything in an enclosing
# scope.

# bad code:
area = 0


def area_of_square(length: float):
    global area  # Refactoring (1.1)
    area = length * length
    # name shadowing (1.0): Shadowing means using the same name, in an inner scope, as a variable in an outer scope.
    # The Python compiler doesn't care if you shadow variables. It knows which one exists in which scope, and doesn't
    # get confused. But using the same name in different places can really confuse us humans.


area_of_square(30)
print(f'The area is {area}')  # The result is 0 without the 'global keyword'. (1.0)
# The result is now 900 with the 'global keyword'. - Refactoring (1.1)
