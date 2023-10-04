#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqueIntegers = set()
    sum = 0
    for index in my_list:
        if index not in uniqueIntegers:
            sum += index
            uniqueIntegers.add(index)
    return sum
