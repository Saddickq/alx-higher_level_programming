#!/usr/bin/python3
def uppercase(str):
    word = ""
    for char in str:
        if (ord(char) >= 97 and ord(char) <= 122):
            word += chr(ord(char) - 32)
        else:
            word += char
    print(f"{word}")
