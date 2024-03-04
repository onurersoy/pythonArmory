def sum_eo(n, t):
    answer = 0
    for i in range(0, n):
        if t == "e" and i % 2 == 0:
            print(t)
            answer += i
        elif t == "o" and i % 2 != 0:
            print(t)
            answer += i
        elif t not in ["e", "o"]:
            print(t)
            return -1
    return answer


answer1 = sum_eo(10, "e")
print(answer1)


# The original solution for the challenge (Section: 6, Coding Exercise: 16)
def sum_eo_new(n, t):
    """Sum even or odd numbers in range.

    Return the sum of even or odd natural numbers, in the range 1..n-1.

    :param n: The endpoint of the range. The numbers from 1 to n-1 will be summed.
    :param t: 'e' to sum even numbers, 'o' to sum odd numbers.
    :return: The sum of the even or odd numbers in the range.
            Returns -1 if `t` is not 'e' or 'o'.
    """
    if t == "e":
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))


x = sum_eo_new(11, 'spam')
print(x)
