# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

print(RED, "this is in red")
# If you do not 'RESET' each colour / effect choice (like the line above^^), it would continue applying to the below
# lines as well. Run this py file and notice!!
print(REVERSE, "this is red and reverse")
print(UNDERLINE, "this is red, reverse and underline")


def colour_print(text: str, effect: str) -> None:
    """
    Print `text` ısing the ANSI sequences to change colour, etc.
    :param text: The text to print.
    :param effect: The effect we want. One of the constants defined at the start of this module.
    """
    output_string = "{0}{1}{2}".format(effect, text, RESET)
    print(output_string)


print(RESET)
colour_print("Hello, Red", RED)
print("This should be in the default terminal colour")
colour_print("Hello, Magenta", MAGENTA)
colour_print("Hello, Reverse", REVERSE)
