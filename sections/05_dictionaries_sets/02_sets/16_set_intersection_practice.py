trial_1 = {"Bob", "Charley", "Georgia", "John"}
trial_2 = {"Anne", "Charley", "Eddie", "Georgia"}

check_set = trial_1.intersection(trial_2)  # << intersection method
print(check_set)
# You can also use 'intersection operator'.
# You can use the operator alternative to find intersection of more than 2 sets too...

print()

farm_animals = {'sheep', 'hen', 'horse', 'cow', 'goat'}
wild_animals = {'lion', 'elephant', 'horse', 'tiger', 'goat', 'panther'}
potential_rides = {"donkey", "horse", "camel"}

intersection = farm_animals & wild_animals & potential_rides
print(intersection)  # << intersection operator

# You can also pass more than 1 sets to '.intersection' method:
mounts = farm_animals.intersection(wild_animals, potential_rides)
print(mounts)
