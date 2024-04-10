# Making sense of data is called parsing. When we talk about parsing data – or parsing code – it means splitting
# it up into logical components.

input_filename = 'country_info'

with open(input_filename) as country_file:
    for row in country_file:
        data = row.split('|')  # '|' << that's the separator that's used on the data itself in this example.
        # print(data)
        # f.e = ['Country', 'Capital', 'CC', 'CC3', 'IAC', 'TimeZone', 'Currency\n']
        # Let's remove the new line '\' at the end of each row. We will re-create the same example in the below section:

with open(input_filename) as country_file:
    for row in country_file:
        data = row.strip('\n').split('|')
        print(data)
