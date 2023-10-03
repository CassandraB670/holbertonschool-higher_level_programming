#!/usr/bin/python3
def max_integer(my_list=[]):
    maxi = my_list[0] if my_list else None
    for index in my_list:
        if index >= maxi:
            maxi = index
    return maxi
