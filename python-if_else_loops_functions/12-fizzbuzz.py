#!/usr/bin/python3
def fizzbuzz():
    result = ""
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            result += "FizzBuzz "
        elif index % 3 == 0:
            result += "Fizz "
        elif index % 5 == 0:
            result += "Buzz "
        else:
            result += str(index) + " "
    print(result, end="")
