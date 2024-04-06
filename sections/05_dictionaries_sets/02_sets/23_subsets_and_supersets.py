animals = {'Turtle',
           'Horse',
           'Robin',
           'Python',
           'Swallow',
           'Hedgehog',
           'Wren',
           'Aardvark',
           'Cat',
           }
birds = {'Robin', 'Swallow', 'Wren'}

print(f'birds is a subset of animals: {birds.issubset(animals)}')  # True
print(f'animals is a superset of birds: {animals.issuperset(birds)}')  # True

print(f'birds is a superset of animals: {birds.issuperset(animals)}')  # False

# Let's check it with the operators:
print(birds <= animals)  # True
print(birds < animals)  # True (it means that 'birds' is also a proper subset of 'animals')
# Notice that the method version does not check for proper subset or proper superset.

print('*' * 80)

garden_birds = {'Swallow', 'Wren', 'Robin'}
print(garden_birds == birds)  # True
print(garden_birds <= birds)  # True
print(garden_birds < birds)  # False (not a proper subset)

print('*' * 80)

more_birds = {'Wren', 'Budgie', 'Swallow'}
print(garden_birds >= more_birds)  # False (not a superset)
