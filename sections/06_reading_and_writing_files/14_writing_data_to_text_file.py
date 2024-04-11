data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flowexr",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

plants_filename = 'flowers_write.txt'

with open(plants_filename, "w") as plants:
    # w = write
    for plant in data:
        plants.write(plant)

# That's definitely different to our previous file (check the result file)! Instead of each plant on a new line, we've
# got a single line of text, with each plant written immediately after the previous one. That's the most obvious
# difference between using 'print' and using 'write'. The write method only sends exactly what you specify to the file.
# 'print' performs various conversions on the data, and includes things like line breaks, and separators.

# About the "various conversions" mentioned above; the print function calls a special method,
# that all objects have, before printing the object. The method's called __str__. We'll learn the reason for that
# strange name, with underscores, in the OOP section. What the method does is return a string representation of the
# object. That's what allows print to print objects to the screen.

filename = "test_numbers.txt"
with open(filename, "w") as test:
    for i in range(10):
        print(i, file=test)
# This will run successfully.

with open(filename, "w") as test:
    for i in range(10):
        test.write(i)
# This will return an error!: "TypeError: write() argument must be str, not int"

# We're writing to a text file, which means we can only put strings into it. The print function will print the string
# representation of any object that you ask it to print. In addition, it will include a separator between multiple
# arguments – the default is a space, but that can be changed with the sep keyword argument. Finally, it will print the
# value of the end keyword argument. The default is a newline character.

# The write method will only write exactly what you tell it to write. No separators or newline characters are included
# unless you explicitly tell it to write them. Also, no conversion is performed. If you tell 'write' to write an
# integer, that's what it will try to send to the file. If the file is opened in text mode (the default), you'll get an
# error if you try to write numerical values to it.

# Let's change that code to write the string representation of our integer values. To get the string representation of
# an object, we use the 'str' function:
with open(filename, "w") as test:
    for i in range(10):
        test.write(str(i) + "\n")
