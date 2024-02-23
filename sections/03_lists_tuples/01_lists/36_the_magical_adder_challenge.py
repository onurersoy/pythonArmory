user_input = input("Please provide 3 numbers: ")
string_tokens = user_input.split(",")

int_tokens = []
for st in string_tokens:
    int_tokens.append(int(st))

a, b, c = int_tokens
result = a + b - c
# result = int_tokens[0] + int_tokens[1] - int_tokens[2]

print(result)
