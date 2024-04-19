import csv

input_filename = 'country_info'

countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    dict_reader = csv.DictReader(country_file, delimiter='|')
    for row in dict_reader:
        # countries[country.casefold()] = country_dict
        countries[row['Country'].casefold()] = row
        # countries[code.casefold()] = country_dict
        countries[row['CC'].casefold()] = row  # 'CountryCode'

# print(countries)

while True:
    chosen_country = input('Please enter the name of a country: ')
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['Capital']}")
    elif chosen_country == 'quit':
        break
