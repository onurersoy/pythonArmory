# A dictionary is a collection of values, that are stored using a key.
# Each value stored in the dictionary has a key. We use the key to get the values from the dictionary.
# You'll find dictionaries as storing key/value pairs. Each value has a unique key, that's used to refer to it.

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

# INDEXING:
my_car = vehicles['fiesta']
print(my_car)

commuter = vehicles['virago']
print(commuter)

# GET METHOD:
learner = vehicles.get("er5")

# Dictionaries also have 'GET' method as shown above. Let's see why we might use it rather than indexing:
# If the key doesn't exist, 'dot get' will return 'None', whereas 'indexing' will crash with a 'KeyError'!
# The 'get' method is useful when you're not sıre if the key exists or not.
# Another reason is that sometimes you want to get an error; 'handling exceptions. Sometimes it's better for the code
# to crash, rather than for it to process invalid data.

# Then why bothering with 'indexing' instead of get method all the time?
# The answer is, indexing is faster.
# If you know that the key will be present, then use indexing...
# If there's a possibility that the key won't be present, then call the get method...
