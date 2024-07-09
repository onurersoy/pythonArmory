# Bubble sort is the simplest sorting algorithm available. It's very basic and isn't used in real applications. It
# is a very useful algorithm for educational purposes though. Because it's so simple, we can concentrate on its
# performance without getting bogged down in the details of how it's implemented.

# The basic idea is that successive pairs of values are compared, and swapped if they're not in order. As a result,
# large values bubble up to the end of the list.

def bubble_sort(data: list) -> None:
    """Sorts a list in place"""
    n = len(data)  # << Function calls take longer to execute than getting the value of a variable. So if you're going
    # to use a function's return value more than once, then bind a variable to the result.
    comparison_count = 0

    for i in range(n - 1):
        for j in range(n - 1):
            comparison_count += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]  # << On the right, we've got a tuple. We unpack the tuple
                # into the variables on the left.

        print(f"End of pass {i}. Data is now {data}")
    print(f"Comparison count is {comparison_count}")
# Alright, that's our Bubble sort algorithm finished^^.


numbers = [3, 2, 4, 1, 5, 7, 6]
print(f"Sorting {numbers}")
bubble_sort(numbers)
print(f"The sorted data is {numbers}")
# Notice that the 'comparison_count' is 36, which is n^2.
