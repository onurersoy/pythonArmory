# Similar to the 'locals()' function, Python has a 'globals()' function to get the global namespace dictionary.
# We can use that, then use normal dictionary indexing to get the value that was stored for one of the names that we
# want to find out:
g = globals()
print(g)
print(g['square'])  # It will give an error since it's not imported on this module.

# You may be wondering how Python managed to find the print function. print doesn't exist in either of those
# dictionaries, so how did Python find it?
# The answer is: There's another namespace that encloses everything. That namespace is the 'builtins' namespace,
# and it stores the names of all the objects that are built into Python. Every built-in function that we've used – such
# as print, or len, or the locals and globals functions that we've just used – exist in the builtins namespace.

# If Python doesn't find a name in the local namespace, it searches the global namespace next.
# If it doesn't find the name in there either, it searches the builtins namespace.

# If the name is found in the builtins namespace, Python can get the object to use. If it's not found there either,
# your code crashes with a NameError exception.

# We're almost ready to see the full rule that Python uses, to resolve names to objects. Almost, but not quite.
# We still need to learn about nested functions first.

# If we pass an object to dir, it'll return the names (as a list) in that object's namespace. Now let's print out
# builtin namespace - or the builtins dictionary:
print(dir(__builtins__))
# You should be able to find False and True, as well as things like print and str (and etc.). These all exist in the
# builtins module, and Python automatically imports that module before loading our program. The builtins module gets
# imported before anything else, giving everything access to the objects in the builtins namespace.

# The reason for the double underscores (dunder) before and after builtins, is to prevent us from accidentally
# redefining the builtins name. When Python imports the builtins module, it mangles the name by adding those
# underscores. If you define something that you call builtins, the real builtin module will still be available –
# because it's renamed to __builtins__ after being imported.

# There's an acronym that's commonly used: 'LEGB'. Standing for Local, Enclosing, Global, Builtins.
# That's the order that Python searches to find a name.
