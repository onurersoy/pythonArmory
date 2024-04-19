import csv

# In the previous examples using CSV files, we examined the datasets in our IDE to get a feel for the
# structure of each file. That's something I suggest you always do, because it helps to visualize what
# you're working with.

# The CSV module can make life easier, by checking the data for you. To do that, we use the
# CSV Sniffer class.

input_filename = 'country_info'

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    country_reader = csv.reader(countries_data, delimiter='|')
    # We have direct access on source data, so we can go and check which delimiter^^ we should use.
    # But let's imagine that you've written a program that fetches files from different sources,
    # automatically. You can't examine each file yourself, to check things like the separators being
    # used.
    # We need an automated solution. The CSV module's Sniffer class can help here!
    # It examines a sample of the file, and works out things like the separators, the character
    # used to delimit strings, and so on. It uses that sample to create a 'Dialect'.
    # A Dialect is just all of the various options, grouped together into a single object.
    for row in country_reader:
        print(row)
# So let's try again, this time with using sniffer class and creating a dialect:

print('*' * 80)

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    sample = countries_data.read()  # Because we've read the entire file, there's nothing left
    # for the reader to read. We've reached the end of the file, and any subsequent read won't
    # find any data. To fix the problem, we need to tell Python to go back to the start of the file!
    # PS. I actually put this note^^ after adding the dialect to below and running the program and
    # noticing that nothing happened.
    # Also notice that reading the whole file isn't efficient when the file itself is huge, we need another way.
    country_dialect = csv.Sniffer().sniff(sample)  # sniff method
    countries_data.seek(0)  # The seek method is used to position the file pointer to another place in the file.
    # Now we will replace the below 'delimeter' with our new 'country_dialect':
    country_reader = csv.reader(countries_data, dialect=country_dialect)
    for row in country_reader:
        print(row)

print('*' * 80)

# We noticed that reading the whole file isn't efficient when the file itself is huge, we need another way:
with open(input_filename, encoding='utf-8', newline='') as countries_data:
    sample = ""
    for line in range(3):
        sample += countries_data.readline()
    country_dialect = csv.Sniffer().sniff(sample)
    countries_data.seek(0)
    country_reader = csv.reader(countries_data, dialect=country_dialect)
    for row in country_reader:
        print(row)
