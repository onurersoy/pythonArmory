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

# Changing items (Change the Virago):
vehicles["virago"] = "Yamaha XV535"

# You can even use your change argument on the dictionary literal (it would appear changed on its original position):
vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple',  # ^^
}

vehicles["starfighter"] = "Lockheed F-104"

# Removing items - FIRST way (very similar with lists & tuples):
del vehicles["starfighter"]  # We are using its key to delete

# Removing items - SECOND way:
# But why we need a '2nd way'? If we try removing an item that doesn't exist, we get an error!
# del vehicles["f1"]
# That's one reason why we have get method.
vehicles.pop("f1", None)
#  So the 'pop' method removes an item from the dictionary and returns the value. If the key doesn't exist, it returns
#  whatever you pass for the default instead which is 'None' here. If we do not pass any value, we get the same error
# with this one: 'del vehicles["f1"]'

# You might return a String too:
result = vehicles.pop("exotic car", "You wish!!")
print(result)

for key, value in vehicles.items():
    print(key, value, sep=", ")
