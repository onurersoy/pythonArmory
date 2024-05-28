# In addition to '13_importing.py', another way to import from another module, is to use
# 'from x import *'. It's similar to explicitly importing the objects you want, but imports almost everything. That can
# be very convenient, but it does have some drawbacks.
# 1. You've no idea what's been imported. It will import almost every object from the module you're importing from.
# You don't know what names will be added to your namespace, so you don't know if any names you define will clash with
# them.
# 2. You also don't know if one module contains the same names as another. If you import * from both of them, a name
# in the second module could replace something from the first one you import (So the second imported one will replace
# the first one and will be used instead).

# But also, importing like 'from x import *' is similar to 'from better_code import area_of_square' so you don't have to
# use the module name prefix. You can directly start using 'area_of_square'.
# But that's one of the few times you should do this in code. It's OK to do it in an interactive shell, but generally
# not in your code. But you can imagine that it's now difficult to tell where things are coming from (remember
# 'turtle.forward()' and 'forward()' examples). That's one reason you shouldn't do this.
