#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0
    if (len(sys.argv) < 2):
        print("{:d}".format(0))
    else:
        for arg in sys.argv[1:]:
            sum += int(arg)
        print("{:d}".format(sum))
