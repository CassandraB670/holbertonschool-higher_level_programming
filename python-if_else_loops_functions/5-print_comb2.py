#!/usr/bin/python3
separate = ", "
for index in range(0, 100):
    if index == 99:
        separate = "\n"
    print("{:02}".format(index), end=separate)
