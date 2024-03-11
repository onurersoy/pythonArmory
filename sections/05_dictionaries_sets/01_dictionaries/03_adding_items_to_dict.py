# Notice that there is no 'append' method for dictionaries
# Instead we assign the value to a dict by using its key:

# noinspection PyDictCreation
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

vehicles["starfighter"] = "Lockheed F-104"
for key, value in vehicles.items():
    print(key, value, sep=", ")

# Dictionaries preserve the insertion order!
