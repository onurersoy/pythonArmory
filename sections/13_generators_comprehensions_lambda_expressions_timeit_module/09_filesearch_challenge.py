import os
import fnmatch


def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        # for artist in directories:
        for artist in fnmatch.filter(directories, artist_name):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                # As we explained earlier, on line 9, using '_' is a Python convention to show that you're not using the
                # value, but have to specify it when doing things like unpacking a tuple or dealing with values returned
                # by a function call.
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):  # we want the path, not the name of the album
            yield song


album_list = find_albums("music", "Aerosmith")
song_list = find_songs(album_list)
# So we're basically chaining generators together by passing one generator on, as the argument to the next.

for s in song_list:
    print(s)

# So generators are really one of those features that make Python an excellent choice for working with huge data sets.
