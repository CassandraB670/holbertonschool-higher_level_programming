#!/usr/bin/python3
""" Script that takes in an argument and displays all values, safe from
MySQL injections!"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name = %s \
            ORDER BY id ASC", [state_name_searched])
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    database.close()
