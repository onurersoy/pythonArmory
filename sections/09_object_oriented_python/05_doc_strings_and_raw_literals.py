a_string = "this is\na string split\t\tand tabbed"
print(a_string)

raw_string = r"this is\na string split\t\tand tabbed"
print(raw_string)

b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

backslash_string = "this is a backslash \followed by some text"
print(backslash_string)
backslash_string = "this is a backslash \\followed by some text"
print(backslash_string)

error_string = r"this string ends with \\"
# We are getting an error, so if you want to end a string with a 'backslash', you have to escape it, even when using
# a 'raw string literal', in other words, we have to put a double backslash in there and that fixes the problem in the
# raw string above.
