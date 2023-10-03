#!/usr/bin/python3
def max_integer(my_list=[]):
    maxi = my_list[0]
    length = len(my_list)
    if my_list == []:
        return None
    for index in range(length):
        if my_list[index] >= maxi:
            maxi = my_list[index]
    return maxi
