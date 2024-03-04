def banner_text(text: str = " ", screen_width: int = 80) -> None:  # 'None', as this method does not intend to return
    # any value
    # Check the lines above^^
    # Check the lines below:
    """

    :param text: The string to print.
        An asterisk (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border at
        the left and right edges.
    :param screen_width: The overall width to print within
        (including the 4 spaces for the ** either side).
    :raises ValueError: If the supplied string is too long to fit.
    :return: !'DELETE THIS ONE AS THIS METHOD DOES NOT INTEND TO RETURN ANY VALUE'!
    """
    # Did you notice this line above?: ":raises ValueError: if the supplied string is too long to fit." It means that
    # you can add different kinds of explanations to your docstring!
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger then specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text()
banner_text(screen_width=60)
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*")
