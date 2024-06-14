# Intro: '12_inheritance_intro.txt'
class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        # Introduced after 'vampire_17_another_enemy_subclass':
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print(f"I took {damage} points damage and have {self.hit_points} left")
        else:
            self.lives -= 1
            if self.lives > 0:
                print(f"{self.name} lost a life")
            else:
                print(f"{self.name} is dead")
                self.alive = False

    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, Hit points: {self.hit_points}"


class Troll(Enemy):
    # This is the only available way in Python 2.
    # def __init__(self, name):
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)
    # So we created an init method for our troll class, and when we did that the init method of 'enemy' is no longer
    # called. You could say that the trolls init method had shadowed init method in its superclass. So to get around
    # that and make sure that class attributes are initialized, we called the enemy superclass's init method, that's the
    # call on line 24 by prefixing the method name with the class name. It's important to remember that we are calling
    # the superclass init method here, and it needs 4 arguments; now our trolls init method only takes two arguments,
    # so we should provide values for the remaining two. So that's one way to do it, and that would be the only way
    # available in Python 2.

    # In Python 3, we can use the super method instead, and if you want to cope with multiple inheritance, you must use
    # super instead of specifying the base class name like we did on line 24. So, to introduce the other approach,
    # let's comment out line 23 and 24 and continue from below:
    def __init__(self, name):
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)
        # What we're basically doing is passing the name of our class troll and the current instance self to super, and
        # then we're using that to call the init method of the base class.

        # The above code line and the below one doing the same thing; the compiler knows the type troll and the instant
        # self, so there's really no need to specify them in the super call. So it's better and easier to define like
        # this:
        super().__init__(name=name, lives=1, hit_points=23)

    # Subclasses can have additional attributes to extend their behavior and allow them to do things that their base
    # class doesn't do, so let's demonstrate:
    def grunt(self):
        print(f"Me {self.name}. {self.name} stomp you")
