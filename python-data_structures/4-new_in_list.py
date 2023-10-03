#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        copy0 = list(my_list)
        return copy0
    else:
        copy1 = list(my_list)
        copy1[idx] = element
        return copy1
