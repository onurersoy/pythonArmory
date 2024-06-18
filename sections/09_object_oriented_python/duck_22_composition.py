class Wing(object):
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Wee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wings = Wing(1.8)  # TODO: Needs to be further investigated
        # COMPOSITION:::
        # We created a new wing object and assign it to the _wing attribute of the duck class, now any duck objects we
        # create will have their own wing object and can use the attributes of a wing (class version) including this
        # case the 'fly' method.
        # Now when a class contains another object like this, that's called 'composition'!

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wings.fly()  # TODO: Needs to be further investigated


class Penguin(object):

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Are you 'aving a larf? I'm a penguin!")


# def duck_test(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()


if __name__ == '__main__':
    donald = Duck()
    # duck_test(donald)
    donald.fly()

    # percy = Penguin()
    # duck_test(percy)
