#!/usr/bin/python3
alphabet = ""
for index in range(97, 123):
    if chr(index) not in ["q", "e"]:
        alphabet += chr(index)
print("{}".format(alphabet), end="")
