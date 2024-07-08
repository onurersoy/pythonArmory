from data import plants_list


def sort_perennials(item) -> str:
    if item.lifecycle.casefold() == 'perennial':
        return '1' + item.name
    else:
        return '0' + item.name


# plants_list.sort(key=sort_perennials)
# Now lets use a lambda instead of passing the name of the function as a parameter:
plants_list.sort(key=lambda item: '1' + item.name if item.lifecycle == 'perennial' else '0' + item.name)
# OK, that's a lambda that uses a conditional expression, to return different values depending on the 'lifecycle' field
# of our plants.

with open('planting_instructions3.txt', 'w', encoding='utf-8') as output_file:
    for plant in plants_list:
        where_to_plant, who = ('windows box', 'me') if plant.lifecycle == 'Perennial' else ('garden', 'gardener')
        print(f"{plant.name}: {where_to_plant}, {who}", file=output_file)
