#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_len = len(sys.argv) - 1
    if (len(sys.argv) < 2):
        print("{:d} {}".format(argv_len, "arguments."))
    else:
        i = 1
        print("{:d} {}".format(argv_len, "arguments:"))
        for arg in sys.argv[1:]:
            print("{:d}: {}".format(i, arg))
            i += 1
