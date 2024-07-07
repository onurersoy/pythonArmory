# It's to allow '28_map_challenge.py' work, so simply ignore it.

text = "what have the romans ever done for us"


def comp_caps():
    capitals = [char.upper() for char in text]
    return capitals


def map_caps():
    map_capitals = list(map(str.upper, text))
    return map_capitals


def comp_words():
    words = [word.upper() for word in text.split(' ')]
    return words


def map_words():
    map_w = list(map(str.upper, text.split(' ')))
    return map_w
