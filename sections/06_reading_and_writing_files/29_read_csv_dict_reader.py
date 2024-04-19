import  csv

# The 'DictReader' works like the reader that we've already used, but produces rows of dictionaries.
#  We can pass the same format options – the delimiter, and so on – to a DictReader as we can for a reader.
# We can also provide a Dialect to specify all the options in a single object.

cereals_filename = 'cereal_grains.csv'

with open(cereals_filename, encoding='utf-8', newline='') as cereals_file:
    reader = csv.DictReader(cereals_file)
    for row in reader:
        print(row)
        # Now notice that each row is a dictionary.
