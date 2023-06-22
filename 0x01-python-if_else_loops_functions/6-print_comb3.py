#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (i < j):
            if (i >= 8):
<<<<<<< HEAD
                print(f"{i:d}{j:d}")
            else:
                print(f"{i:d}{j:d}, ", end="")
=======
                print("{:d}{:d}".format(i, j))
            else:
                print("{:d}{:d}".format(i, j), end=", ")
>>>>>>> e72746654570e76179c938f91f91e7ce173f8906
