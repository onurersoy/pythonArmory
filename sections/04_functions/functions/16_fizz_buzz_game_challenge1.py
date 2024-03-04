def fizz_buzz(n: int) -> str:
    """
    Method version of fiz buzz game
    :param n: The number you provide
    """
    if n % 3 == 0 and n % 5 == 0:
        print("fizz buzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(str(n))


n = input("Provide a number: ")
for i in range(0, int(n) + 1):
    fizz_buzz(i)
