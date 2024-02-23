flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily"
]

for flower in flowers:
    print(flower)

print()

separator = " | "
output = separator.join(flowers)
print(output)  # The 'join' method does the iterating for us on this code (so we did not use a for loop)

print(", ".join(flowers))
# Remember that all the items in the iterable must be string if you want to join the items!
