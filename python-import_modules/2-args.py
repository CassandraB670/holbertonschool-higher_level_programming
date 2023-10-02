#!/usr/bin/python3
import sys

if __name__ == '__main__':
    arguments = sys.argv[1:]
    numberOfArg = len(arguments)
    if numberOfArg == 0:
        print("0 arguments.")
    else:
        moreThanOneArg = "s" if numberOfArg > 1 else ""
        print("{} argument{}:".format(numberOfArg, moreThanOneArg))
    for index, arg in enumerate(arguments, 1):
        print("{}: {}".format(index, arg))
