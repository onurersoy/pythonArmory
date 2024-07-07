from data import plants_list

x = 99

# Conditional expression:::
result = 'in range' if x < 100 else 'out of range'
print(result)
# General syntax:
# <true value> if <condition> else <false value>
# '<true value>' -> This can be any expression, including a number, a string (as in our example) or a function that
# returns a value.
# '<condition>' -> You can use more complex conditions here - anything that evaluates to True or False.
# '<false value>' -> This can be any expression, including a number, a string (as in our example) or a function that
# # returns a value.

print()

with open('planting_instructions.txt', 'w', encoding='utf-8') as output_file:
    for plant in plants_list:
        # if plant.lifecycle == 'Perennial':
        #     where_to_plant = 'windows box'
        # else:
        #     where_to_plant = 'garden'
        where_to_plant = 'window box' if plant.lifecycle == 'Perennial' else 'garden'
        # If we had more complex code in the if and else clauses, then a conditional expression couldn't be used. That
        # doesn't mean we can't assign more than one value: we can use tuple unpacking to give different values to more
        # than one variable. Now check the next module!
        print(f"{plant.name}: {where_to_plant}", file=output_file)
