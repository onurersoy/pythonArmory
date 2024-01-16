number = "9,223;372:036 854,775;807"
seperators = ""

for char in number:
    if not char.isnumeric():
        seperators = seperators + char

print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
