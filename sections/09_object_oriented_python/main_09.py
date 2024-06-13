# Intro: '07_getters_and_setters_intro.txt'

# import player_08 as player
from player_08 import Player

# tim = player.Player("Tim")
tim = Player("Tim")
print(tim.name)
print(tim.lives)
tim.lives -= 1
print(tim.lives)
# Now the attributes such as 'lives' and 'names' are encapsulated in the Player class, but they're not hidden and
# that's something that I'm sure Java and C++ programmers will find horrible because in those languages, providing
# direct access to the data attributes is really frowned upon, but in Python, it's considered the opposite, in other
#  words, the way to do things.

# So the first thing I'm going say about getters and setters in Python is don't use them. Well, actually,
# I don't mean never use them, I mean don't worry about them when you're creating your classes. That's because
# chances are you won't need them, so don't spend time creating getters and setters that won't be needed.

# In Python, getter and setter actually work a bit differently. Now the basic principle is the same, that is to use a
# method to return the value of an attribute or assign a new value to it. But you still use the same syntax as you
# would when accessing the attributes directly. Let's add getter and setter to Player class.

# After creating getter and setter on 'player_08.py', the above code still works perfectly. So we didn't have to make
# a change on our main programme. So it continues to use the Player class in exactly the same way as it did before we
# changed the lives attribute to use the getter and setter methods.

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim._lives = 9
print(tim)
# You can see that that does work, so as I've said a few times, Python doesn't enforce any idea of private variables.
# You're free to change anything you want, but if the creator of the class has hidden that data attribute by prefixing
# its name with an underscore, then you may cause problems if you do go changing it.
