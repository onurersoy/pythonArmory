import csv

# The DictReader automatically reads the column names from the CSV file it's reading, and uses those names
# for the individual dictionary keys. But what happens if the file doesn't contain column headings? There must be
# some way to provide the keys if they're not in a header row in the file. And we also need to provide the keys
# when using a DictWriter to create a CSV file. We can pass a list, containing the keys, to these objects, in the
# fieldnames argument.

input_filename = 'country_info'

dialect = csv.excel
dialect.delimiter = '|'

countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    # Get the column headings from the first line of the file:
    headings = country_file.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()

    # The DictReader and DictWriter objects accept a fieldnames argument. That's optional with a DictReader if the
    # first line of the file contains the column headings. If it doesn't, you'd have to provide a list containing the
    # column headings – or field names. That's why we created line 17.
    dict_reader = csv.DictReader(country_file, dialect=dialect, fieldnames=headings)
    for row in dict_reader:
        # countries[country.casefold()] = country_dict
        countries[row['country'].casefold()] = row
        # countries[code.casefold()] = country_dict
        countries[row['cc'].casefold()] = row  # 'CountryCode'

# print(countries)

while True:
    chosen_country = input('Please enter the name of a country: ')
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['capital']}")
    elif chosen_country == 'quit':
        break
