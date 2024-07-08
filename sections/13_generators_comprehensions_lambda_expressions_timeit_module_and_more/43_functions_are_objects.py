from medals_data import medals_table

# Can we store the functions in the dictionary? Why not? Functions are objects, dictionaries are used to store objects,
# why not store the functions in the dictionary?

# options = {
#     'C': ('country',),
#     'G': ('gold medals',),
#     'S': ('silver medals',),
#     'B': ('bronze medals',),
#     'R': ('rank',),
# }

options = {
    'C': ('country', lambda d: d['country'], False),
    'G': ('gold medals', lambda d: d['gold'], True),
    'S': ('silver medals', lambda d: d['silver'], True),
    'B': ('bronze medals', lambda d: d['bronze'], True),
    'R': ('rank', lambda d: d['rank'], False),
}
# To be clear, we didn't have to use lambdas here. We could have used normal function definitions, and stored the
# function names in the dictionary. This isn't a technique that relies on lambdas, but this did seem to be a good
# example for me to mention it.

while True:
    for option, (description, *_) in options.items():
        # Our code works, because I've used "star" before the second variable in the tuple. That works in a similar way
        # to *args. However, many other values there are (including zero items), they'll be mopped up into another
        # tuple. We don't use those values here, which is why I called the variable underscore. There's nothing special
        # about that name, but it's used by convention to indicate a value that's required, but not used. If you're
        # unpacking a tuple (or list, or anything else that you can unpack), and you don't know how many items it might
        # contain, you can use star to mop up all the remaining values. As I said, it works the same as *args in a
        # function definition.
        print(f'{option}: Sort by {description}')
    print('Invalid choices will exit.')

    # choice = input('Please select an option: ').upper()

    # if choice == 'C':
    #     medals_table.sort(key=lambda d: d['country'])
    # elif choice == 'G':
    #     medals_table.sort(key=lambda d: d['gold'], reverse=True)
    # elif choice == 'S':
    #     medals_table.sort(key=lambda d: d['silver'], reverse=True)
    # elif choice == 'B':
    #     medals_table.sort(key=lambda d: d['bronze'], reverse=True)
    # elif choice == 'R':
    #     medals_table.sort(key=lambda d: d['rank'], reverse=True)
    # else:
    #     break

    choice = input('Please select an option: ').upper()

    description, function, reverse = options.get(choice, (None, None, None))
    # It'll^^ crash if the user types a letter that isn't in the dictionary. To fix that, we provide a default value to
    # the get method: If the choice isn't in the dictionary, we return a tuple containing None for each item.
    if description:
        medals_table.sort(key=function, reverse=reverse)
    else:
        break
    # It has another advantage as well – as I mentioned a few moments ago. If we had other columns to sort on – more
    # options in other words – we don't have to change the code. We just add more entries to the dictionary.

    print(f'Sorted by {description}')
    for row in range(10):
        print(medals_table[row])
