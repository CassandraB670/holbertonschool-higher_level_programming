#!/usr/bin/python3
def roman_to_int(roman_string):

    myDictionary = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0

    if not roman_string or not isinstance(roman_string, str):
        return 0

    prevValue = 0

    for symbol in roman_string:
        value = myDictionary.get(symbol, 0)
        if value > prevValue:
            result += value - 2 * prevValue
        else:
            result += value
        prevValue = value
    return result
