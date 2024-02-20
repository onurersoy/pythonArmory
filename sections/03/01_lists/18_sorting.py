# sorted function can be used to sort any iterable object

pangram = "The quick brown fox jumps over the lazy dog"
# A pangram is a phrase that contains all the letters of an alphabet, at least once.

letter = sorted(pangram)
print(pangram)
# Python sorted function will take any iterable but will always return a list, and the list is in alphabetical order.

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers) # function
print(numbers)
print(sorted_numbers)

numbers.sort() # method
print(numbers) # sorted function sorts it by creating a new list while sort method does not create a new list;
# sort method sorts the list in place!!

new_list = numbers.sort()
print(new_list) # you will get 'None'
# Note. sort method sorts the elements of a list in-place and returns None. It does not produce a new list or any
# other meaningful result. So, after numbers.sort() is executed, 'new_list' will be assigned the value None,
# and that's what gets printed when you use print(new_list). If you want to sort the list and also have a sorted
# copy of the list, you can use the sorted() function like:
missing_letter = sorted("The quick beown fox jumped over the lazy dog")
print(missing_letter)

sorted = sorted(numbers) # Never use a name of a built-in function as it will end with an error!
print(sorted)
