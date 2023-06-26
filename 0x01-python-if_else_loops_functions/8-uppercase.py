#!/usr/bin/python3
def uppercase(str):
    word = ""
    for char in str:
        if (ord(char) >= 97 and ord(char) <= 122):
            word += chr(ord(char) - 32)
        else:
            word += char
<<<<<<< HEAD
    print(f"{word}")
=======
    print("{}".format(word))
>>>>>>> e72746654570e76179c938f91f91e7ce173f8906
