#!/usr/bin/python3
def common_elements(set_1, set_2):
    for index in set_1:
        for index2 in set_2:
            if index2 == index:
                return index
