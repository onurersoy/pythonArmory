# Although they're not a sequence type, they are iterable. We can iterate over the keys in a dictionary.

vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

for key in vehicles:
    print(key)
    print(key, vehicles[key], sep=", ")

print()

# This 2nd approach is way efficient than the 1st one:
for key, value in vehicles.items():
    print(key, value, sep=", ")

# PS. You might come across that inefficient loop if you find yourself modifying or converting old Python 2 code.
# 'dot items' in Python 2 created a list. That means it needed a copy of the data, and used more memory.
# For that reason, programs might have used the simple for loop to avoid the extra memory overhead of using 'dot items'.
# Python 2.2 added a 'dot iteritems' method which works in a similar way to Python 3's 'dot items' method.
# Python 3 now uses something called generator, and doesn't copy the data from the dictionary.

# With Python 3, remember to use 'enumerate' when iterating over sequences, and 'dot items' when iterating
# over dictionaries!
