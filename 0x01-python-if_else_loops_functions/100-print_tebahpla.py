#!/usr/bin/python3
for char in range(ord('z'), ord('a') - 1, -1):
    if ((ord('z') - char) % 2 == 0):
<<<<<<< HEAD
        print(chr(char), end="")
    else:
        print(chr(char).upper(), end="")
=======
        print("{}".format(chr(char)), end="")
    else:
        print("{}".format(chr(char).upper()), end="")
>>>>>>> e72746654570e76179c938f91f91e7ce173f8906
