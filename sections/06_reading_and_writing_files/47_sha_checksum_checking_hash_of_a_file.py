import hashlib

published_hash = '4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6'
# Alright, we've imported the hashlib module, and stored the website's hash as a string. The next step is to read the
# contents of the file we downloaded, and generate the hash for it. If the two hashes are the same, the file hasn't
# been modified.

# I'll use a variable for the filename, then open the file in binary mode, for reading. After that, the next step is to
# generate the SHA-256 hash, and print it out. We'll use the hex-digest method; remember that it returns a string
# representation of the hash. That's why we stored our hash as a string, on line 3.

filename = 'colorama-0.4.6-py2.py3-none-any.whl'

with open(filename, 'rb') as downloaded_file:
    contents = downloaded_file.read()

file_hash = hashlib.sha256(contents).hexdigest()
print(file_hash)

if file_hash != published_hash:
    print(f'The file {filename} has been modified')
else:
    print(f'The file {filename} hash is correct')
