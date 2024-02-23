def is_sentence_palindrome(string):
    result_string = ''.join(char for char in string if char.isalnum())
    return result_string[::-1].casefold() == result_string.casefold()


# 2nd option:
def palindrome_sentence(input_sentence):
    string = ""
    for char in input_sentence:
        if char.isalnum():
            string += char
    print(string)
    return string[::-1].casefold() == string.casefold()  # if the equation is true, it returns 'True', else 'False'


sentence = input("Please enter a sentence to check: ")
if is_sentence_palindrome(sentence):
    print("'{}' is a palindrome".format(sentence))
else:
    print("'{}' is not a palindrome".format(sentence))
# Was it a car, or a cat, I saw?
