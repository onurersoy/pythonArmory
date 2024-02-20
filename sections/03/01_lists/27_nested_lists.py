empty_list = []
even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers1 = even + odd
print(numbers1)

# A list containing two lists:
numbers2 = [even, odd]
print(numbers2)

for number_list in numbers2:
    print(number_list)
    for value in number_list:
        print(value)
        