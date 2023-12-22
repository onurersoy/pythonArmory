parrot = "Norwegian Blue"

print(parrot[0:6])  # Norweg : slice it from position 0 to 6; 6th excluded
# The last character you specify isn't included in the slice on Python
print(parrot[3:5]) # we

print(parrot[0:9])
print(parrot[:9])
# They are both the same^

print(parrot[10:14])
print(parrot[10:])
# They are both the same^

print(parrot[:])
print(parrot)
# They are both the same^

# slicing with negative numbers:
print(parrot[0:6])
print(parrot[-14:-8])
# They are both the same^

print(parrot[-4:-2])
print(parrot[-4:12])
print(parrot[10:12])
# They are both the same^


# Using a Step in a Slice:
print(parrot[0:6:2]) # Nre
# It means from 0th to 6th, ignore every 2nd item^
print(parrot[0:6:3]) # Nw

number = "9,223;372:036 854,775;807"
seperators = number[1::4] # From 1st to the end; ignore every 4th item
print(seperators)
