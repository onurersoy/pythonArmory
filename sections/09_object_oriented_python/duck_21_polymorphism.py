# Intro: '20_polymorphism_intro.py'

class Duck(object):  # TODO: Needs to be further investigated ('object' part!)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack quack")


class Penguin(object):

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Are you 'aving a larf? I'm a penguin!")


def duck_test(duck):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == '__main__':
    donald = Duck()
    duck_test(donald)

    percy = Penguin()
    duck_test(percy)

# So we've created both a duck class and a penguin class.It's clear that the penguin isn't a duck, but it happens to
# have exactly the same methods as our duck class, and consequently we can do exactly the same things with the penguin
# comparing with the duck.

# So you can see that our test_duck function still works, percy may will be behaving a little bit strangely by duck
# standards. However, as far as the test_duck function concerned, percy walks like a duck, swims like a duck and quacks
# like a duck. So in other words, our Percy is a duck just like our Donald.

# Duck test is a humorous term for a form of reasoning and boils down to being able to tell what something is by how it
#  behaves, and the phrase is attributed to an American poet James Whitcomb Raleigh, and his original phrase was:
# When I see a bird that walks like a duck swims like a duck and quacks like a duck, I'll call that bird a duck.

# So what's the point of all this? Well, that approach is fundamental to the way that Python deals with objects unlike
# statically typed languages that require the type of every object to be declared.
# Python's dynamic typing means that it's only really interested in what can be done with an object. If an object has
# the necessary attributes, then Python is quite happy for it.

# Now the phrase is commonly used in dynamically type languages like Python, and you'll often hear them referred to as
# duck-type. Now we know that penguins aren't ducks, but Percy has inherited any of these duck-like behaviour.

# The important thing is that Percy has the methods that our test_duck function relies on and so as far as Python is
# concerned, Percy is a duck.
