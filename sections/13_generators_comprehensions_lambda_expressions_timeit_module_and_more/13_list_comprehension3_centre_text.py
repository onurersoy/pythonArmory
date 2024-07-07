def centre_text(*args):
    # text = ""
    # for arg in args:
    #     text += str(arg) + " "

    # Let's refactor above:
    text = "-".join([str(args) for arg in args])  # << list comprehension
    # Note:
    # text = "-".join(str(args) for arg in args)  # << This (without square brackets) would produce the same outcome,
    # but it then would be a generator comprehension, and we will talk about them later.
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)
centre_text("spam, spam, spam and spam")

centre_text("first", "second", 3, 4, "spam")
