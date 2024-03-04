def fizz_buzz(n: int) -> str:
    """
    Play fiz buzz
    :param n: The number to check
    :return: 'fizz' if the number is divisible by 3.
        'buzz' if it's divisible by 5.
        'fizz buzz' if it's divisible by both 3 and 5.
        The number, as a string, otherwise.
    """
    if n % 15 == 0:
        return "fizz buzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)


x = 100
for i in range(0, x + 1):
    print(fizz_buzz(i))
