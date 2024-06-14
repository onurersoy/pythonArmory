# Intro: '12_inheritance_intro.txt'

from enemy_15_calling_super_methods import Enemy, Troll
from vampire_17_another_enemy_subclass import Vampire

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
