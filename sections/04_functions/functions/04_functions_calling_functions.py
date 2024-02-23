def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(input_sentence):
    string = ""
    for char in input_sentence:
        if char.isalnum():
            string += char
    print(string)
    return is_palindrome(string)


sentence = input("Please enter a sentence to check: ")
if palindrome_sentence(sentence):
    print("'{}' is a palindrome".format(sentence))
else:
    print("'{}' is not a palindrome".format(sentence))
# Was it a car, or a cat, I saw?
