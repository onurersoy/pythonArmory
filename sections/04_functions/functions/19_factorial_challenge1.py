def factorial(n: int) -> int:
    """
    This method calculates the factorial value of the given number
    :param n: The number given
    :return: Returns an int value which equals to factorial values of n
    """

    if n in (0, 1):
        return 1
    if n > 1:
        answer = 1
        for i in range(2, n + 1):
            answer *= i
        return answer


for i in range(36):
    print(i, factorial(i))
