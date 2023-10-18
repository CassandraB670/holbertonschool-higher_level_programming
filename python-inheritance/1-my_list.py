#!/usr/bin/python3
"""write a class that inherits from list"""


class MyList(list):
    """class that inherits frome list"""

    def print_sorted(self):
        """print list"""

        if issubclass(MyList, list):
            print(sorted(self))
