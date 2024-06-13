# Intro: '07_getters_and_setters_intro.txt'

# So the convention is that class name should start with a capital letter.
class Player(object):

    def __init__(self, name):  # << Class constructor
        self.name = name
        # self.lives = 3
        self._lives = 3
        self.level = 1
        self.score = 0
        # We have four data attributes. 1 of them is a parameter for creating an instance of this class. The other three
        # values start with default values 3, 1 and 0.

    # Adding getter and setter:
    # So the first thing we are going to do is hide our 'lives' attribute^^ by prefixing it with an underscore.
    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    # Now once again, we're hiding these methods^^ by starting their names with an underscore. Of course, they're not
    # really hidden as such. However, there's no need for clients to use them directly and the underscore at the
    # start of the name gives users of our class an indication that they shouldn't really be calling these methods.

    # The last step is to define a 'property' called 'lives' that uses these two methods when reading and writing our
    # lives attribute:
    lives = property(_get_lives, _set_lives)
    # It's very important that the data attribute mustn't have the same name as the property.Now we could have
    # renamed the 'lives' attribute to anything, as long as it wasn't the same name as we used for the property. So it
    # makes sense just to put a prefix with an underscore because that hides the attribute as well.

    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, Level: {self.level}, Score: {self.score}"
    # The above function manages what will be printed out when you print your object/instance
