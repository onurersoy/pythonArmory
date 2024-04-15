import csv

csv_filename = 'OlympicMedals_2020.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    # Reading csv seemed to work fine without 'newline' argument. But the footnote states that things might not
    # work correctly without it. It also says that you might get strange results when writing a CSV file if you
    # don't provide an empty string for the newline argument. So I'm going to do as the documentation tells us to,
    # and include that argument when opening a file.
    headers = csv_file.readline().strip('\n').split((','))
    # After line 10 executing, the file pointer moves to the next line of the file. That means the reader will
    # start reading from the second line, skipping the headers. This behaviour is caused by 'readline' method
    # as we mentioned before.
    print(f'Column headers: {headers}')
    reader = csv.reader(csv_file)
    # The reader function returns a reader object, that we can use to iterate over the lines in the file. Each
    # line will be parsed into fields, and we'll get a list for each row.

    # The CSV module provides another way to do this, and can create a dictionary with those headings as the key
    # as we will examine it later.
    for row in reader:
        print(row)
        # We've read the column headings into a list, and the reader function processes the
        # data rows. We do have a problem with our lists though:
        # The numerical values have been parsed as strings, not integers. The reader function has an option
        # that can help with that, but unfortunately, it only works when string values are surrounded with quotes.
        # As we saw, our country names aren't quoted. We will look at that option later, but it's not going to
        # work with this file. We could unpack each of the values into variables, and use the int function to convert
        # the integer values tho:
    for rank, country, gold, silver, bronze, total in reader:
        print(int(rank), country, int(gold), int(silver), int(bronze), int(total))
