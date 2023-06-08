#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_len = len(sys.argv) - 1
    if (len(sys.argv) < 2):
        print("{:d} arguments.".format(argv_len))
    else:
        i = 1
        if (argv_len == 1):
            print("{:d} argument:".format(argv_len))
        else:
            print("{:d} arguments:".format(argv_len))
        for arg in sys.argv[1:]:
            print("{:d}: {}".format(i, arg))
            i += 1
