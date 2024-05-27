print(dir())
# The output is a list, containing all the names that exist in our module's namespace.
# About double underscore ('__'), it's pronounced 'dunder'. That's much easier to say than "underscore underscore" or
# "double underscore".

import turtle
# The name "turtle" appears in this module's namespace. Note that turtle is the only name that's been imported from
# the turtle module. If we want to use any of the functions, such as forward, we have to use turtle.forward. Python
# then checks the turtle module to find the forward function.

from math import radians, cos
# We imported two functions from the math module. When we import objects in this way, the names of the objects are put
# into the importing module's namespace. We have radians and cos in this namespace, but we don't have math
# ('from math import math'). If we try to refer to math in our code, we'll get an error. 'math' doesn't exist in this
# module's namespace. Because we've imported those names into the module's namespace, we can use radians and cos in
# our code. There's no need to prefix them with 'math.'. In fact, if we did try to use math.cos, we'd get an error.

# We've seen that a namespace is a container for the variable names.

# 'Scope' is where that variable exists. When we talk about the scope of a variable, we mean the places in our code
# where it can be used. For example, the scope of the cos function, in our code, is the entire module. We can call the
# cos function from anywhere in our module (it means this .py file, where we imported the function), and it will be
# found. That's because we imported it into the global namespace for the (this) module.

# 'Global scope' is the entire module while 'local scope' is f.e. the function (so that variable can only be used
# inside of that function).

# In Python, there are only 3 things that can create a new scope:
# 1. modules
# 2. functions
# 3. classes
# Each of these objects has its own namespace. You can use 'print(dir())' inside a function too, so you can list the
# namespaces (local namespaces) that had been defined in the function (Those names are local to the function, and
# aren't defined outside of it).

# Python also has a 'locals()' function, that does a simlar thing to 'dir()'. We can use it to display the names that
# are local to a function or method. Whereas the dir function only gives us the names, in a list, the locals function
# shows the namespace dictionary.

# Local objects only exist inside the scope where they are defined. They don't exist outside of it, and you'll get an
# error if you try to use the objects in the main code – or inside another function. That's all that scope means. It's
# where an object exists – or where it can be used.

# Note that the same name can be used in more than one function and those wouldn't be referring to the same object.
# You can safely use the same names in different functions, because each one will be local to the function that it
# appears in.

# In summary, scope is where something exists - where you can use it, in other words. The namespace is where the names
# are stored.
