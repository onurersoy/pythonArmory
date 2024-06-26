# Everything in Python is an object. Everything even types is implemented as classes. Object-oriented programming
# uses classes and methods to provide an object that encapsulates both data and the functions that operate on that Data.

# Method is just another word for function. We use it interchangeably but to make it correct; when a function is part of
# a class in Python, we call it a method.

# The convention is to start class names with a capital letter and to use camel case, that's the general naming
# convention in Python.
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

    # The other aspect that I want to mention is that classes also have attributes; the term of 'instance variable' is
    # useful because it contains the word 'instance', now the data attributes in the kettle example as such as 'name'
    # and 'price' have both been attributes of the instances and each  instance has its own values for them, so it's
    # also possible for the class to have attributes which is shared by all the instances:
    power_source = "electricity"


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

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

# To check namespaces:
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
# When we try to access the 'power_source' attribute for the instances Python checks to see if the power source exists
# in the instance name space, if it doesn't, which is the case here, then checks the class for the instance and finds
# 'power_source' in the Kettle class and that's how it printed out because basically it got it from the class attribute.

print("Switch to atomic power")
Kettle.power_source = "atomic"
print("Switch kenwood to gas")
kenwood.power_source = "gas"
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
