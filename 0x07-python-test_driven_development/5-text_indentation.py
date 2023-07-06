#!/usr/bin/python3
"""
module indents a sample text
"""


def text_indentation(text):
    """A function that indents a text"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    length = len(text)
    j = 0
    for i in range(length):
        if length > j:
            print(text[j], end="")
            if text[j] in ['.', '?', ':']:
                print("\n")
                j += 1
        j += 1
    print()
