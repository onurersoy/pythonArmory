# frozenset = It's the immutable version of a set, other than that it's exactly a set (You can't update this set)

# 'union': Creates a new set
farm_animals = {'sheep', 'hen', 'horse', 'cow', 'goat'}
wild_animals = {'lion', 'elephant', 'horse', 'tiger', 'goat', 'panther'}

all_animals_1 = farm_animals.union(wild_animals)  # << 'union method'
print(all_animals_1)  # Notice that it removes the duplicated items.

all_animals_2 = wild_animals.union(farm_animals)
print(all_animals_2)  # It's the same result. It doesn't matter which way round you do it (a + b = b + a)

all_animals_3 = wild_animals | farm_animals  # << 'union operator'
print(all_animals_3)  # It's the same result. It's the same thing as using '.union'.

# Note that union method has an advantage over union operator because you can pass an 'iterable' to the method.
# The operator one would only accept another 'set'.
# The union method is also more readable than the operator.
