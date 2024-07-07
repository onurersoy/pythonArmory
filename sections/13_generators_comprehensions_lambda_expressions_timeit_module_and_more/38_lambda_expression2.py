from medals_data import medals_table


# def sort_country(d: dict) -> str:
#     return d['country']
#
#
# def sort_gold(d: dict) -> str:
#     return d['gold']
#
#
# def sort_silver(d: dict) -> str:
#     return d['silver']
#
#
# def sort_bronze(d: dict) -> str:
#     return d['bronze']
#
#
# def sort_rank(d: dict) -> str:
#     return d['rank']


options = {
    'C': ('country',),
    'G': ('gold medals',),
    'S': ('silver medals',),
    'B': ('bronze medals',),
    'R': ('rank',),
}

while True:
    for option, (description, *_) in options.items():
        print(f'{option}: Sort by {description}')
    print('Invalid choices will exit.')

    choice = input('Please select an option: ').upper()

    if choice == 'C':
        medals_table.sort(key=lambda d: d['country'])
        # d > parameter
        # d['country'] > expression (which is what the function will return)
        # Lambdas can only contain a single expression. They are equivalent to very simple functions that just evaluate
        # and expression and return the result.
        # You can't have code blocks inside a lambda, they can only contain one expression.
        # Python does have conditional expressions (sometimes called a "ternary operator" in other languages). That
        # means you can&nbsp;&nbsp; use the equivalent of if/else in a lambda, but they're still limited to a single
        # expression.
    elif choice == 'G':
        medals_table.sort(key=lambda d: d['gold'], reverse=True)
    elif choice == 'S':
        medals_table.sort(key=lambda d: d['silver'], reverse=True)
    elif choice == 'B':
        medals_table.sort(key=lambda d: d['bronze'], reverse=True)
    elif choice == 'R':
        medals_table.sort(key=lambda d: d['rank'], reverse=True)
    # We've now replaced all 5 of those small functions, with a lambda. Lambda functions can be useful, but they haven't
    # allowed us to do anything that we couldn't do with functions. The resulting code is a lot shorter. It's also
    # probably more readable, because you don't have to scroll around to find the function definitions, to see what
    # those functions were doing.
    else:
        break

    print(f'Sorted by {options[choice][0]}')
    for row in range(10):
        print(medals_table[row])
