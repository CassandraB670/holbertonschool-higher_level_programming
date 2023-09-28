#!/usr/bin/python3
def uppercase(str):
    uppercaseStr = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            uppercaseLetter = chr(ord(char) - 32)
        else:
            uppercaseLetter = char
        uppercaseStr += uppercaseLetter
    print("{:s}".format(uppercaseStr))
