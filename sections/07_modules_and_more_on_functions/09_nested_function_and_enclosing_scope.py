def greet_pythons(items: list) -> None:
    greeting = 'Hello'

    def make_greeting(item: str) -> str:
        # return f'Hello {item}'
        return f'{greeting} {item}'

    for item in items:
        print(make_greeting(item))


names = ['John', 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']

greet_pythons(names)

# When a name isn't found in the local scope, Python searches the enclosing namespace.
# The enclosing namespace for our make_greeting function is the greet_pythons function. The name greeting is found in
# the enclosing scope, and we can use it inside our nested function. That's all that enclosing scope means. When a
# function or method is contained inside another one, the containing function is its enclosing scope.
