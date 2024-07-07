# Lambda expression is an expression that creates an anonymous function.
# Anonymous function means a function that doesn't have a name.
# It seems they are generally less useful than they are in languages like Java.
# A lambda is an expression, which means we can use it anywhere that an expression appears.
# A lambda expression evaluates to a function, and that function is then used as the value of the expression.

from medals_data import medals_table


def sort_key(d: dict) -> str:
    return d['country']


medals_table.sort(key=sort_key)  # >> We are passing the function as an argument
print(medals_table)


def double(x):
    return x * 2


print(double)

# Lambda syntax:::
print(lambda x: x * 2)
