# Intro: '12_inheritance_intro.txt'

from player_08 import Player
from enemy_13_subclasses_and_overloading import Enemy, Troll

tim = Player("Tim")
print(tim)
random_monster = Enemy("Basic Enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(8)
print(random_monster)

random_monster.take_damage(9)
print(random_monster)


ugly_troll = Troll()
print(f"Ugly troll - {ugly_troll}")

another_troll = Troll("Ug", 18, 1)
print(f"Another troll - {another_troll}")

brother = Troll("Urg", 23)
print(brother)

# So when you overload a method in other programming languages, you provide a method with exactly the same name but
# taking different arguments. So the ugly troll constructor on line three doesn't take any arguments and another_troll
# constructor on line six takes or gets three arguments, and his brother Urg has two arguments. Now in Java, you'd need
# to write three constructors, one for each case. However, Python doesn't have the concept of overloaded methods.

# Also remember that we defined some default values for the constructors on the base class which is 'Enemy'.

# You can't actually overload functions and methods in Python, but you can generally get the same effect by using named
# parameters with default values.

# Additional note: Method Overloading in Java is a feature that allows a class to have more than one method with the
# same name, but with different parameter lists. Overloading is a form of polymorphism, which is a core concept in
# object-oriented programming.
