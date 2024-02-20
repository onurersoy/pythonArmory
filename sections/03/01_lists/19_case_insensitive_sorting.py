pangram = "The quick brown fox jumps over the lazy dog"

letter = sorted(pangram)
print(pangram)


numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(numbers)
print(sorted_numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick beown fox jumped over the lazy dog",
                        key=str.casefold)
print(missing_letter)

missing_letter2 = "The quick beown fox jumped over the lazy dog"
missing_letter3 = sorted(missing_letter2.casefold())
print(missing_letter3)

names = ["Graham", "John", "terry", "eric", "Terry", "micheal"]
names.sort(key=str.casefold())
print(names)
