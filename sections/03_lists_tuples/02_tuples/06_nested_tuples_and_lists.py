albums = ["Welcome to my Nightmare", "Alice Cooper", 1975,
          "Bad Company", "Bad Company", 1974,
          "Nightflight", "Budgie", 1981,
          "More Mayhem", "Emilda May", 2011,
          "Ride the Lightning", "Metallica", 1984,
          ]

print(len(albums))  # 15

# Now let's store them as tuples:
albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

print(len(albums))  # 5

for name, artist, year in albums:
    # 1st way to unpack the tuple^^
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

for album in albums:
    name, artist, year = album
    # 2nd way to unpack the tuple^^
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))
    #      .format(album[0], album[1], album[2]))
