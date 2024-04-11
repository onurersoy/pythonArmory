# Python generally uses UTF-8 by default in many systems.
# On Windows, in particular, the 'open' method generally doesn't default to UTF-8.

# The text files that we include in the resources for the videos are encoded in UTF-8.
# If you download text files from the internet, that's probably the encoding those files will use too.

# In Python 2, you had to explicitly specify that a string is encoded using one of the encodings specified in the
# Unicode standard (check '16_unicode_in_python.py'). You had to prefix the string with the letter "u", to create a
# Unicode string.
# In Python 3 – which is what we're using - all strings are Unicode. That makes life a lot easier because we don't
# have to concern ourselves with converting between ASCII and our Python strings.  If you attempt to read a file
# containing text using a different script, or alphabet, Python supports that. But you do have to be aware of the
# encoding that was used.
