# Intro: '12_inheritance_intro.txt'
from enemy_15_calling_super_methods import Enemy


class Vampire(Enemy):
    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, Hit points: {self.hit_points}"

    def dodges(self):
        import random
        if random.randint(1, 3) == 3:
            print(f"**** {self.name} dodges *****")
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


# Inheritance challenge:
class VampireKing(Vampire):  # Subclass of a subclass
    def __init__(self, name):
        super().__init__(name)  # TODO : Needs to be further investigated
    # Notice the single parameter we use when calling the super init method on line 28. Now our vampire class is a
    # subclass of enemy and vampire king is a subclass of vampire, so the method that will be called when we use super
    # init here is actually the vampire class init method and not the enemy init method.
    # Now the init method in the vampire class will then call init in the enemy class, so the calls will pass
    # up the chain with each subclass calling the init method of its superclass.
        self.hit_points = 140

    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, Hit points: {self.hit_points}"

    def take_damage(self, damage):
        # if not self.dodges():  # << No need for this as vampire king extends from vampire and use its take_damage
        # method, so it already has the 'dodge' feature. So it's already overriding the original method.
        super().take_damage(damage=damage // 4)
