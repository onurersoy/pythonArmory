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

plants_filename = 'flowers_print.txt'

with open(plants_filename, "w") as plants:
    # w = write
    for plant in data:
        print(plant, file=plants)
        # 'file=' argument of 'print' tells Python to print where it should print the data to. The default is to print
        # to the screen. But you can print to any output stream that can accept text – including to an 'open file'.

        #  Anything that we can print to the console can also be sent to a file, instead.

# Now let's read the data back:
# After opening the file for reading, we iterate over it, and add each string to the new_list list:
new_list = []
with open(plants_filename, "r") as plants:
    for plant in plants:
        new_list.append(plant.rstrip())

print(new_list)

# Printing data to a file is quite easy as it's shown on the above using 'print'. But this isn't the only way.
