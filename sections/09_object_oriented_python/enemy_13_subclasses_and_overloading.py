# Intro: '12_inheritance_intro.txt'
# Also be noticed that we are still going to use our game project we created for getters and setters.
class Enemy:
    # class Enemy(object):  # Both declarations are the same. So 'Enemy' actually inherits from 'object'. It's mostly
    # for Python 2 so do not use it.

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print(f"I took {damage} points damage and have {self.hit_points} left")
        else:
            self.lives -= 1

    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, Hit points: {self.hit_points}"


class Troll(Enemy):
    # It means Troll inherits from Enemy / Troll extends from Enemy
    # Troll is a subclass, Enemy is a base/superclass
    pass
