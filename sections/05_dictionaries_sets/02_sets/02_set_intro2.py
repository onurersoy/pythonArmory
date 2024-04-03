farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farm_animals)
# The items will be printed without an order (sets are unordered)

# Another way to demonstrate that, is to see what happens when we iterate over our set.
# Sets aren't a sequence type – sequence types are ordered, so a set can't be one – but we can still iterate over
# a set:

for animal in farm_animals:
    print(animal)
# Run it a couple of times and notice that the items appear disorder

# Because sets use hashes to store the items, anything that you want to put into a set must be hashable.
# That's exactly the same requirement that we had for dictionary keys.

# You can't index into a set; it means 'set' object is not subscriptable.
# If items in a set don't have a fixed position, then it just doesn't make sense to try to get an item at a certain
# position.
# It also means that you can't slice a set.

print()

more_animals = {'goat', 'sheep', 'hen', 'horse', 'cow'}
# 'farm_animals' and 'more_animals' are two equal sets, let's check:
if farm_animals == more_animals:
    print("Sets are equal")
else:
    print("Sets are different")
# Order is not important when comparing two sets!^
# That's a different behaviour to lists and tuples. Lists and tuples will compare equal if they contain the same
# items, in the same order.
