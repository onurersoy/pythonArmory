import os

root = "music"

for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)
        first_split = os.path.split(path)
        print(first_split)
        second_split = os.path.split(first_split[0])
        print(second_split)
        for f in files:
            # song_details = f.strip('.emp3').split(' - ')
            song_details = f[:-5].split(' - ')
            print(song_details)
        print("*" * 40)
# Okay, 'os.walk' is a generator, so it doesn't try to read every single file and directory at once into a huge list.
# It's only yielding the details for a single directory at a time. So ultimately, we could have millions of albums, and
# we can process them in this way without running out of memory. So generators can get even more useful when you use
# them to create other generators, and we'll start working on that in the next module.
