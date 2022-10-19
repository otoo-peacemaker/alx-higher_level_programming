#!/usr/bin/python3
"""This is the ``5-text_indentation`` module"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ?, :

            Args:
                text (str): The text to print
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    text_len = len(text)
    seps = ".?:"
    i = 0
    lines = ""

    while True:
        while i < text_len and text[i] == " ":
            i += 1
        if i == text_len:
            break

        start = i
        while i < text_len and text[i] not in seps:
            i += 1

        if i == text_len:
            i -= 1
            while i > start and text[i] == " ":
                i -= 1

        i += 1

        line = text[start:i]
        if line:
            lines += line
            if line[i - start - 1] in seps:
                lines += "\n\n"

    print(lines, end="")
