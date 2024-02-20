data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

del data[0]
print(data)
del data[0:2]
print(data)
del data[14:]
print(data)

min_valid = 100
max_valid = 200

data2 = [4, 5, 104, 105, 110, 120, 130, 130, 150,
         160, 170, 183, 185, 187, 188, 191, 350, 360]
# Be very careful when changing the size of an object that you're iterating over:
for index, value in enumerate(data2):
    if (value < min_valid) or (value > max_valid):
        del data[index]
# An errored example^^
