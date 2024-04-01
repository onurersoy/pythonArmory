data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy"),
]


def simple_hash(s: str) -> int:
    """A ridiculously simple hashing function"""
    basic_hash = ord(s[0])
    return basic_hash % 10


def get(k: str) -> str:
    """Return the value for a key, or None if the key doesn't exist"""
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


keys = [""] * 10
values = keys.copy()

# Our simple dictionary implementation:
for key, value in data:
    h = simple_hash(key)
    # h = hash(key)
    print(key, h)
    keys[h] = key
    values[h] = value
    # We calculate the hash of the key, and use that to index into the 'values' list.

print(keys)
print(values)
print()
value = get("lemon")
print(value)

# We're using all this^ to demonstrate how a dictionary uses a hash table.
