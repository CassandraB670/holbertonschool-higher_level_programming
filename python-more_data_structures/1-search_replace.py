#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = []
    for index in my_list:
        if index == search:
            index = replace
            newList.append(index)
        else:
            index = index
            newList.append(index)
    return newList
