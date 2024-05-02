# For our second example working with binary files, we're going to read the tags in an MP3 file.

# The MP3 coding format is a way to digitize audio, while keeping the file size small. It achieves small file sizes by
# using lossy compression.

# No information is lost when you compress data into a zip file. When you unzip the zip file
# archive, you get back exactly the same data that was originally compressed.

# MP3 loses information when the audio is compressed. It approximates some sounds and throws others away. You can't
# uncompress an MP3 file, and get back the original audio that was recorded. In practice, this isn't a problem. MP3 is
# intended to be played on small computer loudspeakers, and hand-held portable music players. Although there is a loss
# of quality, the format is adequate for the systems it's intended to be played on.

# Originally, MP3 files didn't contain any information about the audio they contained. When you play an MP3 file on
# your phone, or some other device, you expect to see the name of the song, and the band that recorded it. It's also
# common to have the album cover appear on the device's screen (if it has one). None of that information is catered
# for in the MP3 specification. ID3 is a specification for a meta-data container. It allows things like the artist,
# album, and song title to be included in the MP3 file. It's worth noting that it hasn't been approved by any
# organization. But it has become a de facto standard, and most MP3 players will read the ID3 tags and display the
# information they contain.

# For this example, we'll have a look at extracting the ID3 tags from an MP3 audio file ('46_read_id3.py'). We'll also
# extract the cover image – if there is one – and save it in a separate file.
