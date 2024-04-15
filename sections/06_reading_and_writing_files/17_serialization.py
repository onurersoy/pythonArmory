# Serialization: The process of translating a data structure or object state into a format that can be stored (for
# example, in a file or memory data buffer) or transmitted (for example, over a computer network) and reconstructed
# later (possibly in a different computer environment).

# The whole point of serializing something is so that you can either store it somehow, or send it somewhere else.
# 'reconstructed later': If we can't deserialize the data, to get it back, then there was little point serializing it
# in the first place.

# If serialized data is going to be useful to different programs and computer systems, then it needs to follow a
# well-defined standard.
# JSON is one such standard (ISO = The International Standards Organization)
