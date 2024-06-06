# Everything in Python is an object. Everything even types are implemented as classes.
# Object-oriented programming uses classes and methods to provide object that encapsulates both data and the functions
# that operate on that Data.

# Method is just another word for function. We use it interchangeably but to make it correct; when a function is part of
# a class in Python, we call it a method.

class Kettle(object):
    # Looking at below, it can be helpful to think of a class as a template from which objects it can be created.

    def __init__(self, name, price):
        # Functions that are bound to a class called methods and the main difference between a method and a function
        # is the presence of this 'self' parameter.
        # It's a reference to the instance of the class.
        self.name = name
        self.price = price
        self.on = False
        # The term 'Constructor' refers to a special method executed when an instance of a class is created or
        # constructed in Python; this is the 'init' method.
    # All the objects created from the same class will share the same characteristics.
    # An instance is just another name for an object created from a class definition. So if I now create a kettle
    # called 'Kenwood', then Kenwood will be an instance of the kettle class.

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)  # Creating 'kenwood' instance from 'Kettle' class.
print(kenwood.name)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)
print(f"Models: {kenwood.name} = {kenwood.price}, {hamilton.name} = {hamilton.price}")

# Remember that 'kenwoord' and 'hamilton' are also objects.

# Attributes: So we've become used to talking about variables, but when a variable is bound to an instance of a class
# then it's referred to as a data attribute in Python. You might find variable attributes also called fields in
# languages such as Java or data members in C++.

# There's another way to use a string replacement fields that is useful when dealing with classes so because Kenwood and
# Hamilton are objects, and we can specify their attributes in the replacement fields:
print("Models: {0.name} = {0.price}, {1.name} = {1.price}".format(kenwood, hamilton))
# It's similar to this:
# print("Models: {} = {}, {} = {}".format(kenwood.name, kenwood.price, hamilton.name, hamilton.price))

"""
Class: Template for creating objects. All objects created using the same class will have the same characteristics.
Object: An instance of a class.
Instantiate: Creating an instance of a class.
Method: A function defined in a class.
Attribute: A variable bound to an instance of a class.
"""

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

# Python automatically provides a reference to the instance as the first parameter to the method, now we can see this
# in a bit more detail by not using and instance but calling the method to the class itself:
Kettle.switch_on(kenwood)
print(kenwood.on)

# Remember that variables in Python come into existence the first time they're assigned a value, and the same thing is
# true for instance variables:
kenwood.power = 1.5
print(kenwood.power)
