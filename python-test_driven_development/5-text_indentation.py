#!/usr/bin/python3
"""define a function that prints a text with
2 new lines after each of these characters . ? and :"""


def text_indentation(text):
    """print a text with 2 new lines after . ? and :

    Args:
        text(str): text to print

    Raises:
        TypeError: if text isn't a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])
    print("{}".format(text), end="")
