import better_code

# When you import a module, all the code in the module is executed. That's how importing works in Python.
# After importing, any function you define in another module can be used in your current module without
# re-defining/creating that function. But remember that all the code in the imported module will be executed as well.

#area = better_code.area_of_square(30)
#print(area)
# Notice that running this module also prints the rest of the unwanted part from 'better_code.py'. Now'lets comment-out
# the above parts.

# OK, now let's change the import, to explicitly import just the function we want:
from better_code import area_of_square
area = area_of_square(30)  # Notice that we directly put the function name without its module name because of the way we
# imported the function. But also notice that the result is the same with the previous scenario. Importing them
# explicitly means you don't have to prefix them all with the module name.
print(area)

# So those two different ways of importing do almost exactly the same thing. The code in the imported module gets
# executed, exactly the same whichever way we import. In terms of memory used, there's no difference between the two
# ways of importing.

# You can also change the name of things that you're importing. That's sometimes done when you use something a lot,
# and it has a long name. For example, you might see the tkinter module aliased as tk It's still obvious where the
# mainloop function comes from, but now it's less typing.

# Also you can go like this:
import math
from math import pi as PI
# Now, we can use PI in our code, without qualifying it with the name of the math module, but we also have access to
# all the other math functions such as math.cos.
# Both ways work fine, and one doesn't use more memory than the other. In this example, Python doesn't actually import
# math a second time. It just adds the name PI to the importing module's namespace.


area = better_code.area_of_square(30)
area = area_of_square(30)
# You can probably work out why line 37 is slightly faster than line 36. Think in terms of looking up the names in the
# namespace dictionaries.When you use a fully qualified name, as we're doing on line 36, the module name is looked up
# in the global namespace dictionary. When it's found, Python then has to look up the object's name in the module's
# namespace dictionary. Line 37 only involves a single lookup in the global namespace. If – and only if – you often
# call the function, such as inside a loop where performance is critical, then importing the object explicitly may be a
# better option.
# But unless you really do need to get the very last bit of performance out of your code, favour readability, and what
# comes naturally to you, over importing explicitly for performance reasons. Most of the time, the improvement in
# performance won't be worth sacrificing readability for.
