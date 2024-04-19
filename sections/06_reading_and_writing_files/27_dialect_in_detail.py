import csv

input_filename = 'country_info'
with open(input_filename, encoding='utf-8', newline='') as countries_data:
    sample = ""
    for line in range(3):
        sample += countries_data.readline()
    country_dialect = csv.Sniffer().sniff(sample)
    country_dialect.skipinitialspace = True
    countries_data.seek(0)
    country_reader = csv.reader(countries_data, dialect=country_dialect)
    for row in country_reader:
        print(row)

print('*' * 80)
attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace',
              ]

for attribute in attributes:
    print(f'{attribute}: {getattr(country_dialect, attribute)}')
    # With 'skipinitialspace' set to False, leading spaces won't be trimmed from the data. If you want to trim
    # them, you can set that to True. Let's do it above^^.

# A dialect can be useful if you're reading many files in the same format. You can pass the same dialect to the
# reader, rather than copying all the arguments when calling the reader function.

# It's hard to tell exactly what that lineterminator value is. When you tell Python to print a string containing
# line feeds, it prints new lines. We want to see the actual characters that lineterminator contains. We've seen
# that the print function calls the str function, to get a string representation of the objects. Python has
# another function, that also returns a string, but in a format that's more useful for programmers.
# The function's called 'repr'. Now run the program again, to see the difference that repr makes. It behaves
# differently depending on what you pass to it. In the case of strings, it includes special characters such as \n,
# rather than obeying them. That's often more useful when printing things for diagnosing bugs. We can see that
# the lineterminator contains two characters, a carriage return and a line feed. OK, that's the repr function.
# You may want to use it, instead of str, when printing strings that you suspect might contain special characters.
# You'd only use it for diagnostic information; it's not usually something that you'd display to the users of
# your programs.
print(f'{attribute}: {repr(getattr(country_dialect, attribute))}')
