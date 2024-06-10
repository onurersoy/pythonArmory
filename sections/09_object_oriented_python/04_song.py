class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the song's creator.
        duration (int): The duration of the song in seconds. It may be zero.
    """

    def __init__(self, title, artist, duration=0):
        """Song init method

        Args:
            title (str): Initialises the 'title' attribute
            artist (Artist): At an Artist object representing the song's creator.
            duration (Optional[int]: Initial value for the 'duration' attribute.
                Will default to zero if not specified.
            """
        self.title = title
        self.artist = artist
        self.duration = duration


help(Song)
help(Song.__init__)
print(Song.__doc__)
print(Song.__init__.__doc__)

# We could also add the docStrings to '__init__' method like this:
Song.__init__.__doc__ = """Song init method

        Args:
            title (str): Initialises the 'title' attribute
            artist (Artist): At an Artist object representing the song's creator.
            duration (Optional[int]: Initial value for the 'duration' attribute.
                Will default to zero if not specified.
            """


class Album:
    """ Class to represent an Album, using its track list

    Attributes:
        name (str): The name of the album
        year (int): The year was album was released.
        artist (Artist): The artist responsible for the album. If not specified,
        the artist will default to an artist with the name "Various Artists".
        tracks (List[Song]): A list of the songs on the album.

    Methods:
        addSong: Used to add a new song to the album's track list.
        """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
            song (Song): A song to add.
            position (Optional[int]): If specified, the song will be added to that position
                in the track list - inserting it between other songs if necessary.
                Otherwise, the song will be added to the end of the list.
            """
        if position is None:
            self.tracks.append(self)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details.

    Attributes:
        name (str): The name of the artist.
        albums (List[Album]: A list of the albums by this artist.
            The list includes only those albums in this collection, it is
            not an exhaustive list of the artist's published albums.

    Methods:
        add_album: Use to add a new album to the artist's albums list
        """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (Album): Album object to add to the list.
                If the album is already present, it will not be added again (although this is yet to be implemented).
        """
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of artist, album, year, song
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(f"{artist_field}:{album_field}:{year_field}:{song_field}")

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                # We've just read details for a new artist
                # Store the current album in the current artist's collection then create a new artist object
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                # We've just read a new album for a new artist
                # Store the current album in the artist's collection then create a new album object
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            # Create a new song object and add it to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

            # After read the last line of the text file, we will have an artist and album that haven't been store - process
            # them now!
            if new_artist is not None:
                if new_album is not None:
                    new_artist.add_album(new_album)
                artist_list.append(new_artist)

        return artist_list


def create_checkfile(artist_list):
    """Create a check file from the object data for comparison with the original file"""
    with open("checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print(f"{new_artist.name}\t{new_album.name}\t{new_album.year}\t{new_album.title}",
                    file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    print(f"There are {len(artists)} artists.")

    create_checkfile(artists)

# Programming languages deal with a system known as 'garbage collection' and that means that the runtime system keeps
# track of variables and reclaims their memory when they are no longer being used in the program any more, and that
# generally means even when they go out of scope or when there is no longer anything else referring to them.
