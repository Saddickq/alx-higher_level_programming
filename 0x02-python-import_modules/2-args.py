#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_len = len(sys.argv) - 1
    if (len(sys.argv) < 2):
        print("{:d} arguments.".format(argv_len))
    else:
        i = 1
        print("{:d} arguments:".format(argv_len))
        for arg in sys.argv[1:]:
            print("{:d}: {}".format(i, arg))
            i += 1
