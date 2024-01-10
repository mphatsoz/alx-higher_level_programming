#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num_args = len(argv) - 1
    arg_plural = "s" if num_args != 1 else ""
    end_char = ":" if num_args > 0 else "."

    print("Number of argument{}{}{}".format(arg_plural, "s" if num_args != 1 else "", end_char))

    for i in range(1, num_args + 1):
        print("{}: {}".format(i, argv[i]))
