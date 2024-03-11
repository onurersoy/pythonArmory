def sum_numbers(*values: float) -> float:
    """
    Function to sum the given numbers
    :param values: Desired numbers to sum
    :return: Returns the total sum value
    """
    result = 0
    for number in values:
        result += number
    return result


print(sum_numbers(5, 9))

# 2nd Option (Solution using builtin):


def sum_numbers(*values: float) -> float:
    """ calculates the sum of all the numbers passed as arguments """
    return sum(values)


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
