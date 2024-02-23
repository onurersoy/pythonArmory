welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

# metallica[0] = "Master of Puppets"
# The code above line would return an error as tuples do not support item assignment; it means they're immutables
# That's the main difference between a tuple and a list. Tuples are immutable.

# Because they don't have the overhead of the methods needed to change them, tuples use less memory than lists (The 1st
# reason) That's one reason why you might want to use a tuple!

# There are another couple of reasons for preferring a tuple over a list. Both reasons are due to tuples being
# immutable.
# The first reason is to protect the integrity of your data (The 2nd reason)

metallica2 = list(metallica)  # To create a list from the tuple called 'metallica'
print(metallica2)

metallica2[0] = "Master of Puppets"
print(metallica2)

metallica3 = tuple(metallica2)  # To create a tuple from the list called 'metallica2'
