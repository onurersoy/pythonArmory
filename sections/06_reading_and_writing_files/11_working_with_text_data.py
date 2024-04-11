input_filename = 'country_info'

with open(input_filename) as country_file:
    for row in country_file:
        data = row.strip('\n').split('|')
        # Before we create a dictionary that we use, it would be nice to put all these fields into variables. We can
        # unpack the list for each country:
        country, capital, code, code3, dialing, timezone, currency = data
        # If the list has more than 7 items, it would crash trying to unpack into the above 7 variables^^.
        print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        # Right at the top of the output, the first row in the file contained the headings for the fields. That can
        # be useful, but we don't want to include those entries in our dictionary. The simplest way to exclude them
        # is to read that first line before we iterate over the remainder of the file. Let's do it on the below:

print('*' * 80)

countries = {}
# Refactoring:
with open(input_filename) as country_file:
    country_file.readline()
    # Our 'country_file' object is iterable. Each time you use the 'readline' method to read a line, the iterator
    # automatically moves on to the next item.
    for row in country_file:
        # So our for loop starts with the second line of the file – because we've already read the first line.
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        print(country_dict)
        # What we need now is some way to choose the country. We'll start by choosing a country by name. That means we
        # need to put each of these dictionaries in another dictionary, with the key being the country name.
        countries[country.casefold()] = country_dict
        # code_lookup[code.casefold()] = country

print(countries)

# CHALLENGE:
input_country = input('Please provide the country you wish to see its capital: ').casefold()
print(countries[input_country.casefold()])
if input_country in countries:
    country_data = countries[input_country]
    print(country_data['capital'])

# CHALLENGE REFACTORING:
while True:
    input_country = input('Please provide the country you wish to see its capital: ')
    country_key = input_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {input_country} is {country_data['capital']}")
    elif input_country == 'quit':
        break
