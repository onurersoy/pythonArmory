from data import plants_list

with open('planting_instructions2.txt', 'w', encoding='utf-8') as output_file:
    for plant in plants_list:
        # if plant.lifecycle == 'Perennial':
        #     where_to_plant = 'windows box'
        #     who = 'me'
        # else:
        #     where_to_plant = 'garden'
        #     who = 'gardener'
        where_to_plant, who = ('windows box', 'me') if plant.lifecycle == 'Perennial' else ('garden', 'gardener')
        print(f"{plant.name}: {where_to_plant}, {who}", file=output_file)

# OK, that's conditional expressions in Python^^. Other languages, such as Java, achieve the same thing with what's
# called a 'ternary operator'. So when you come across the term 'ternary operator', that's a 'conditional expression' in
# Python.
