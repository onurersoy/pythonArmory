# In the previous module, we said that the scope free variables defined in can't be the global scope. A variable you
# define at the module level cannot be a free variable, so remember that a global variable can't be a free variable.
# This is important because we have to use a different keyword when dealing with global variables.

# The two keywords we're going to look at are nonlocal and global. If we want to change the value of a free variable,
# we use the nonlocal keyword.
def greet_pythons(items: list) -> None:
    greeting = 'Hello'
    print(id(greeting))

    def make_greeting(item: str) -> str:
        #  What happens if you really do want to change the value of a variable that was defined in an outer scope?
        # The first thing I'm going to say about this is that you should try very hard not to. Try to make your
        # functions as self-contained as possible. If you change something in a scope that doesn't define it, you can
        # end up with bugs that are very hard to diagnose. Sometimes, those bugs don't show up in testing. They can be
        # very dependent on the actual data that your code is working with, and could go unnoticed for months or years.
        # That makes them very expensive to fix. And also remember that just because you can change it, you still should
        # avoid doing that. It's often an indication that the design of your code can be improved.
        # If you really do want to change greeting in the outer function, you have to explicitly tell Python that
        # that's what you want to do. The way we do that is to use the nonlocal keyword:
        nonlocal greeting
        print(id(greeting))
        greeting = 'Hi'
        print(id(greeting))
        return f'{greeting} {item}'

    for item in items:
        print(make_greeting(item))
    print(f'Inside greet_pythons, greeting is: {greeting}')
    print(id(greeting))


names = ['John', 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']

greet_pythons(names)
