# Methods of creating new lists:
empty_list = []
even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

even.extend(odd)
print(even)

sorted_numbers = sorted(numbers)  # sorted function creates a new list called 'sorted_numbers'
print(sorted_numbers)

# if you want to sort a list in place (without creating a new list), use .sort method
numbers.sort()
print(numbers)

digits = sorted("432985617")
print(digits)  # It returns a new list with the chars of string 'digits' as separate char items in a sorted way

digits = list("432985617")
print(digits)  # It returns a new list with the chars of string 'digits' as separate char items

more_numbers = list(numbers)  # 'list' function here creates a new list from the list 'numbers'
print(more_numbers)

print(numbers is more_numbers)  # To check if they are the exact same list or not (FALSE because 'list' function
# creates a new list by copying the original list)
print(numbers == more_numbers)  # To check if they have the exact same items or not (TRUE because 'list' function
# creates a new list by 'copying the original list')

more_numbers2 = numbers[:]  # Creating a new list by 'slicing' the list > not an efficient method
more_numbers3 = numbers.copy()  # Creating a new list by calling 'copy' method
