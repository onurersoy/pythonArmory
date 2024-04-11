input_filename = 'country_info'

countries = {}
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
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
        countries[country.casefold()] = country_dict
        countries[code.casefold()] = country_dict
        # The 'countries' dictionary will now contain two references to the dictionaries for each country. One with the
        # country name as the key, and another with the country code as the key. Note that the individual country
        # dictionaries are not duplicated. As we saw in the last section, 'countries' is storing references to the
        # individual dictionaries. They're not being copied. The dictionary will use more memory, of course. But not
        # significantly more than creating another dictionary.

print(countries)

while True:
    input_country = input('Please provide the country name or country code you wish to see its capital: ')
    country_key = input_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        if country_data.get('input_country') is None:
            print(f"There is no capital of {input_country}")
        else:
            print(f"The capital of {input_country} is {country_data['capital']}")
    elif input_country == 'quit':
        break
