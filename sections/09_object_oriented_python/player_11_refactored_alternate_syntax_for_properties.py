# Intro: '07_getters_and_setters_intro.txt'

class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("Level can't be less than 1")

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    # An alternate syntax for properties:

    @property  # (This is the getter)
    def score(self):
        return self._score

    @score.setter    # (This is the setter)
    def score(self, score):
        self._score = score

    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, Level: {self.level}, Score: {self.score}"
