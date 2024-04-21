import csv

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

# 'Zip' function is in the standard library.
# You pass iterables to it, and it returns an iterable containing tuples. If you provide two lists, for example, each
# tuple will contain two items - one from each list, in turn.
# Passing three lists will create tuples containing three items each.

keys = ['album', 'artist', 'year']

filename = 'albums.csv'
with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=keys)
    for row in albums:
        # print(row)
        zip_object = zip(keys, row)
        print(zip_object)
        for thing in zip(keys, row):
            print("\t", thing)  # You will notice that each object contains 3 tuples.
            # OK, but why is this useful? We've seen that we can pass an iterable of key/value pairs to the dict
            # function to create a dictionary. Our zip objects are iterables, containing key/value pairs. That's
            # exactly what we need if we want to transform our data into a list of dictionaries.
            albums_dict = dict(zip_object)
            print(albums_dict)
            # We've created exactly what a DictWriter needs, to write a CSV file. We can put that code inside a with
            # block, and use a DictWriter to produce a CSV file from the data. Now let's open a file, and use a
            # DictWriter above (line 17)^^
            # The last step is to write each row to the file:
            writer.writerow(albums_dict)

# This example demonstrates how easy it is in Python, to transform your data into a format that you need. Whenever
# you're working with data that's not in a format that you'd like, check out the standard library. Python is a very
# powerful language for working with data, and it's usually very easy to transform your data into different formats.
