# Intro: '12_inheritance_intro.txt'

from enemy_15_calling_super_methods import Enemy, Troll
# from vampire_17_another_enemy_subclass import Vampire
from vampire_18_overriding_methods import Vampire
from vampire_19_inheritance_challenge import VampireKing

ugly_troll = Troll("Pug")
print(f"Ugly troll - {ugly_troll}")

another_troll = Troll("Ug")
print(f"Another troll - {another_troll}")

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()
brother.take_damage(3)

monster = Enemy("Basic enemy")
# monster.grunt()  # << It would give an error, because Enemy class doesn't have 'grunt' method.

print()

dracula = Vampire("Dracula")
print(dracula)
dracula.take_damage(12)

while dracula.alive:
    dracula.take_damage(1)
    print(dracula)

# After 'vampire_18_overriding_methods.py' > 'dodges' method:
print("*" * 80)
dracula2 = Vampire("Dracula2")
while dracula2.alive:
    if not dracula2.dodges():
        dracula2.take_damage(1)
        print(dracula2)

# After 'vampire_18_overriding_methods.py' > 'take_damage' method (overriding 'take_damage' method):
print("*" * 80)
dracula3 = Vampire("Dracula3")
while dracula3.alive:
    dracula3.take_damage(1)
    print(dracula3)

dracula3.lives = 0
dracula3.hit_points = 1
print(dracula3)
# Note that we can't prevent code from accessing the data attributes of our classes, what we can do is providing
# indication that this shouldn't be done, and if you remember the convention is to prefix the attribute names with an
# underscore. Now ideally, we would have done this right from the start, and in fact, I'd recommend prefixing your
# class data attributes with an underscore right away if you decide you want that to you want to hide them. If you do
# find that you need to access them directly, you can refactor the ones that do require direct access.

# Now keep in mind that the Python philosophy is that you probably shouldn't hide them unless modifying them directly
# will break your code somehow.

# After 'vampire_19_inheritance_challenge.py' VampireKing class:
king_of_vamps = VampireKing("MightyVamp")
print(king_of_vamps)
king_of_vamps.take_damage(12)
print(king_of_vamps)
