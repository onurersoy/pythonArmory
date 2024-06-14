# Intro: '12_inheritance_intro.txt'
from enemy_15_calling_super_methods import Enemy

# So as well as adding extra behavior to our subclasses, we can also change the behavior of methods that exists in
# the superclass. Like 'take_damage' method.


class Vampire(Enemy):
    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, Hit points: {self.hit_points}"
