def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string  # If the evaluation is correct, the function will return 'True', else 'False'
    return string[::-1].casefold() == string.casefold()


result = is_palindrome("1221")
print(result)

word = input("Please enter a word to check: ")
if is_palindrome(word):  # if is_palindrome(word) == True
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))
