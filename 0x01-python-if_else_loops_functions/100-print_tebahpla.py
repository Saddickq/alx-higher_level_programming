#!/usr/bin/python3
for char in range(ord('z'), ord('a') - 1, -1):
    if ((ord('z') - char) % 2 == 0):
        print("{}".format(chr(char)), end="")
    else:
        print("{}".format(chr(char).upper()), end="")
