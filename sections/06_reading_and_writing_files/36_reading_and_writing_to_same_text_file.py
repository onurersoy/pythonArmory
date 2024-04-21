# Random Access: It is the term used for accessing data from any part of a file.
# RAM: Random Access Memory
# The computer can read from (and write to) any location in its memory. Random access in files means the same thing.

# The file pointer can be changed to any location in the file, for reading and writing. This file pointer keeps track
# of where you are in the file. It's a bit like your cursor when you're moving around your Python code. When you
# write data to the file, data is written at the current position of the file pointer. The file pointer then moves
# forward, as data is written. That's the same behavior as when you type in a text file. As you type, the text is
# entered at the current cursor position, and the cursor then moves forwards as each character is typed. When reading
# from a text file, reading takes place from the file pointer's position. Once again, the file pointer moves forward
# as data is read.

# Random access in Python is very limited with text files. It's possible to position the file pointer relative to the
# start of the file or position it at the end of the file, but those are the only options available. If you want true
# random access to your text data, you'd have to either open the file in binary mode or read the entire file into a
# string. In practice, that's not a serious limitation. It's rare that you'd want full random access to a text file.
# One practical application might be if you were writing a text editor – such as IntelliJ. But because disk access is
# so slow compared to RAM, you wouldn't work on the disk anyway. You'd read the file into memory, in chunks if it's a
# very large file, and work with the text in RAM. We've seen the seek method that we can use to position the file
# pointer at the start of the file. With text files, we only have 2 options when seeking: we can seek relative to the
# start of the file, or we can seek to the end of the file. And I do mean to the end of the file there. You can't
# seek backwards from the end; you can only go directly to the end of the file. It is possible to seek to a position
# further on from the start of the file, and that's what we'll do in this example.

import datetime
from os import SEEK_SET
from typing import TextIO

# Check 'invoices.csv' to understand what kind of data we are working on.

def get_year() -> int:
    """Return the current year as an integer."""
    return datetime.datetime.now().year


def parse_invoice_number(invoice_number: str) -> tuple[int, int]:
    """Split a well-formed invoice "number" into its component parts.

    :param invoice_number: A string of the form YYYY-NNNN
        YYYY is the 4 digit year.
        NNNN is a 4 digit invoice number, left padded with zeros.
        The 2 parts are separated with a "-" character.
    :return: The returned tuple will contain:
        the 4 digit year as an integer,
        the invoice number as an integer.
    """
    year, number = invoice_number.split('-')
    return int(year), int(number)


def next_invoice_number(invoice_number: str) -> str:
    """ Produce the next invoice "number" in sequence.

    The format of `invoice_number` is described in `parse_invoice_number`.

    :param invoice_number: A string representing an invoice number.
    :return: A string representing the next invoice number.
        The numerical part will be incremented, unless the current year
        isn't the same as the year in `invoice_number`. In that case,
        the new invoice number will contain the current year, and the
        numerical part will be set to "0001".
    """
    invoice_year, number = parse_invoice_number(invoice_number)
    year = get_year()
    if year == invoice_year:
        number += 1
    else:
        invoice_year = year
        number = 1
    new_invoice_number = f'{invoice_year}-{number:04d}'  # << The number part should be padded on the left with zeros.
    # We do that using a format specifier – refer to the 'String formatting' if you need to remind yourself about
    # format specifiers.
    return new_invoice_number


def record_invoice(invoice_file: TextIO,
                   company: str,
                   amount: float) -> None:
    """Create a new invoice number, and write it to a file on disk.

    :param invoice_file: An open text file, opened using r+.
    :param company: The name of the company being invoiced.
    :param amount: The amount of the invoice.
    """
    last_row = ''
    # We need to read the last one from the file. There are a few ways to do that. You could use the readlines method
    # to get all the lines in a list. You can then slice the list to get the last item. The disadvantage of that
    # approach is that the entire file is read into memory. That could be a problem, with very large files. So I'm
    # going to read the file, line by line, to get the last line.
    # We initialise 'last_row' to an empty string, on line 85. That's important, because the file might be empty. If
    # there are no lines of text in the file, we won't enter the for loop, and last_row would be undefined.
    # Initialising it avoids that problem. When the loop terminates, we'll either have the last line of the file,
    # or an empty string.
    for line in invoice_file:
        print('*', end='')  # TODO delete after testing
        last_row = line
    if last_row:
        # invoice_number, _, _ = last_row.split('\t')  # '_' means the 2nd and 3rd unpacked items won't be used anywhere
        # within our application, so no point to focus on them. We could also refer them with a char or word like we
        # always do. However, in this case, it would harm the readability of our code and confuse others as they would
        # try to understand where the other items will be used.
        # Also using '_' will prevent warning messages like 'this variable is never used' etc.
        # Let's comment-out that line and show the 2nd way of:
        invoice_number = last_row.split('\t')[0]
        new_invoice_number = next_invoice_number(invoice_number)
    else:
        # if the file is empty, we'll start numbering from 1.
        year = get_year()
        new_invoice_number = f'{year}-{1:04d}'

    print(f'{new_invoice_number}\t{company}\t{amount}', file=invoice_file)
# Now also let's comment-out the below test code as we don't need it anymore and we can start using the above functions
# outside of test scenarios:

data_file = 'invoices.csv'
with open(data_file, 'r+') as invoices:
    record_invoice(invoices, 'ACME Roadrunner', 18.40)
    # That worked because we opened the file using the mode r+. Think of that as opening in read mode, plus the other
    # mode. You can also use w+, which will also let you read and write to the same file. But the behaviour is very
    # different when the file is opened. Remember that opening a file in write mode will truncate the file, if it
    # already exists. That means all the contents will be deleted. Using w+ as the mode will behave in the same way.
    # It opens the file in write mode, plus the other mode – which is read, this time. But we'll always start off with
    # an empty file, because write mode clears out the existing data when the file is opened. Obviously, that wouldn't
    # be suitable here. We want to keep the existing contents, so we use r+.
    record_invoice(invoices, 'Squirrel Storage', 320.55)
    #  The first line we write will be correct, but any subsequent lines will all have the invoice number 0001.
    # Storing the position of the file pointer, then restoring it before reading from the file again, will fix the
    # problem. Python lets us position the file pointer with the 'seek' method. We can store the file pointer's
    # position by calling the 'tell' method. We'll fix the bug in our code, using those two methods. Check the next
    # .py file.

# Test code:
# current_year = get_year()
# test_data = [
#     ('2019-0005', (2019, 5), f'{current_year}-0001'),
#     (f'{current_year}-8514', (current_year, 8514), f'{current_year}-8515'),
#     (f'{current_year}-0001', (current_year, 1), f'{current_year}-0002'),
#     (f'{current_year}-0023', (current_year, 23), f'{current_year}-0024'),
# ]
#
# for test_string, result, next_number in test_data:
#     parts = parse_invoice_number(test_string)
#     if parts == result:
#         print(f'{test_string} parsed successfully')
#     else:
#         print(f'{test_string} failed to parse. Expected {result} got {parts}')
#
#     new_number = next_invoice_number(test_string)
#     if next_number == new_number:
#         print(f'New number {new_number} generated correctly for {test_string}')
#     else:
#         print(f'New number {new_number} is not correct for {test_string}')
#
#     print('-' * 80)
