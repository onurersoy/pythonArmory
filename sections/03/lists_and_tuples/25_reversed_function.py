# Removing rogue values from an unsorted list backwards

data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200

# for index in range(len(data) - 1, -1, -1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)
#         del data[index]

top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]

# 2nd solution is more efficient for a list with lots of items as it uses enumerate and it's more efficient comparing
# with index look-ups.

# Re-check section 5.112 : Algorithms Performance
# Since the list was in order:
# 1. Index slice backwards (The most performance way since it gets the advantage of the list being in order and delete
# the items at once; 2 & 3 deleting the items one by one)
# 2. Enumerate reversed (2 over 3 if the list is big enough)
# 3. Index backwards

print(data)
