import csv

# Check 'cereal_grains.csv' file and notice that all the strings are enclosed in double quotes. That's not the
# case for most of the csv files. But in this case, that makes it easy for the CSV module to determine the
# type of each field, and I recommend you do this when creating your own CSV files.
# Let's use the CSV module to parse this data, and see the advantage that correctly quoted strings provide

csv_filename = 'cereal_grains.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    # If we tell the reader function that they are quoted, the reader function can take care of converting
    # the numerical values to their correct types.
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)
        # Now check the values and notice that we've got floats rather than strings.
        # But it does have some limitations. The main limitation is that it only works with data that has all
        # string values quoted. The other problem is that the numerical values are all floats. That's probably
        # fine, most of the time, but it is something to be aware of. If you need integer values to be converted
        # to ints (not floats), then you can't use this approach.
