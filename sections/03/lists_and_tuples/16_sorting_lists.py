even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
print(even)

# even.sort()
even.sort(reverse=True)
print(even)

# Now note here that the list has been changed. We didn't get a new list created tho. The contents of 'even' have been
# rearranged. Now that can be important when dealing with very large lists. The items in the list are sorted without
# creating a copy of the list. The sort method doesn't create a copy of the list - it rearranges the items in the list.
# You'll also see this technique described as 'sorting the list in place'.
