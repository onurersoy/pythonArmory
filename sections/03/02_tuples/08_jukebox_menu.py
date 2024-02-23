albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

SONGS_LIST_INDEX = 3  # Whenever you see a name all in capitals, it means it represents a 'constant' and you shouldn't
# change it.
SONG_TITLE_INDEX = 1
# A constant is a fixed value that doesn't change^^

while True:
    print("Please choose your album (invalid choice exits):")
    # for index, (title, artist, year, songs) in enumerate(albums):  # Enumerate function can only return 2 values!
    #     print("{}: {}, {}, {}, {}"
    #           .format(index + 1, title, artist, year, songs))

    # for index, value in enumerate(albums):
    #     title, artist, year, songs = value
    #     print(index, title, artist, year, songs)

    # The 2 for loops above are basically the same things^^

    # Let's build the jukebox menu now:
    for index, (title, artist, year, songs) in enumerate(albums):  # Enumerate function can only return 2 values!
        print("{}: {}".format(index + 1, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break

    # print(albums[choice - 1])
    # print(songs_list)
    # print()

    print("Please choose your song:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONGS_LIST_INDEX]
    else:
        break

    print("Playing {}".format(title))
    print("=" * 40)
