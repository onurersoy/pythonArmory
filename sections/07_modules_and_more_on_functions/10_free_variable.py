# We know that searching for a namespace and an object might become inefficient:
# LEGB: Local, Enclosing, Global, Builtins

# To make things more efficient, Python puts free variables into the local namespace:
# A free variable is a variable that's used in a scope, but that isn't defined there. The name 'greeting' is defined
# in the outer function – the function greet_pythons. It's used in the make_greeting function. That's fine, remember
# that variables defined in an enclosing scope become available in the inner scopes. The name greeting is also added
# to the namespace for the make_greeting function. That avoids the need to search the enclosing scope, because it'll
# be found in the local scope. The Python designers made the decision to do that, and it does make finding these names
# more efficient. So 'greeting' is called a free variable. It's defined in an outer scope, and used in an inner one.
# That's all that the term free variable means.
def greet_pythons(items: list) -> None:
    greeting = 'Hello'
    print(greeting)
    print(id(greeting))

    def make_greeting(item: str) -> str:
        # return f'Hello {item}'
        greeting = 'Hi'
        print(id(greeting))
        return f'{greeting} {item}'

    for item in items:
        print(make_greeting(item))
    print(f'Inside greet_pythons, greeting is: {greeting}')
    print(id(greeting))
    # This will be printed as "Hello". If you assign a new value to a variable that's defined in an enclosing scope,
    # Python creates a new local variable. so it's no longer a free variable. The variable greeting, in the inner
    # make_greeting function, is no longer referring to the same object as greeting in the outer greet_pythons
    # function. Note that this has nothing to do with strings being immutable. We'd get the same behaviour if
    # greeting was a list, or another mutable object.


names = ['John', 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']

greet_pythons(names)

# But there is a restriction that you might not expect. If the name exists in two different namespaces, what happens
# if you bind the name to a new value in the inner scope? The entry in both namespaces would need to be updated.
# That's a problem, because Python doesn't know that it exists in the outer scope. It searched the make_greeting
# namespace, and found the name. There was no reason for it to look further. So it doesn't know – at runtime – that
# there's also another entry. To prevent any problems, Python doesn't allow a free variable to be bound to a new value.

# About the free variables, the scope they're defined in can't be the global scope. A variable you define at the module
# level cannot be a free variable, so remember that a global variable can't be a free variable. This is important
# because we have to use a different keyword when dealing with global variables.

# The two keywords we're going to look at are nonlocal and global. If we want to change the value of a free variable,
# we use the nonlocal keyword.
