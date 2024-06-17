# Intro: '12_inheritance_intro.txt'
from enemy_15_calling_super_methods import Enemy


class Vampire(Enemy):
    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, Hit points: {self.hit_points}"

# Overriding a method: Changing the behavior of a method so a subclass can implement the method from its superclass
# and actually do things differently comparing how it behaves from its baseclass.

    # This def is about 'overriding methods':
    def dodges(self):
        import random  # << Just to demonstrate that it can be imported this way too. But normally, don't do this way.
        if random.randint(1, 3) == 3:  # To generate a random integer between 1, 2, and 3.
            print(f"**** {self.name} dodges *****")
            return True
        else:
            return False

# Alright, so we've added a new method to the vampire class to give them the ability to dodge. What we really want is
# for that behavior to be built into the class rather than our main program, having to check that during each attack.
# So, to do that, we're going to override the take_damage method that the vampire class inherits from enemy...

# Now don't confuse overriding a method with overloading it as I mentioned earlier; overloading doesn't exist in Python
# so if you're not sure what it is, then don't worry because you can't actually do it.

# Anyway, but overriding a method that means replacing it with another one. Now, in languages such as Java and C++,
# there are restrictions on the definition of an overriding method. In Python, you just write a new method with the same
# name as the one that you want to override, the new method doesn't even have to have the same or accept the same
# number of parameters. Although it usually will so.
#
# Let's override the enemy class's take_damage method to make it do something different in the vampire subclass...
    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)
