#!/usr/bin/python3
for alphabet in range(97, (122 + 1)):
    if (alphabet == 101 or alphabet == 113):
        continue
    print("{}".format(chr(alphabet)), end="")
