# Not all functions return a useful value. Some functions, like 'print', and the '.sort' method of lists, perform an
# action.

# A function that's bound to an instance of a class is called a method

# Put 2 empty lines before and after defining a function

def multiply():
    result = 10.5 * 4
    return result


answer = multiply()
print(answer)


# On debugger:

# 1. Step Over: Executes that line without stepping into any functions on that line.
# 2. Step Into My Code: The program execution has jumped to line 9. We've entered the code in our multiply function.
# When you want to check the code in your functions, remember to use the Step into my code button.
# 3. Step Into: It does the same thing at the moment. You won't see a difference until you start splitting your code
# into different modules.


def multiply_new(x, y):  # 'x, y' = Parameters / Formal Parameters
    result = x * y
    return result


answer_new = multiply_new(10.5, 4)  # '10.5, 4' = Arguments / Positional Arguments
print(answer_new)


for val in range(1, 5):
    two_times = multiply_new(2, val)
    print(two_times)

# Functions let you split up a problem into simple steps, with a separate function for each step.
# It's much easier to debug small pieces of code - and it's also much easier to write code - if you break it down into
# small pieces.
