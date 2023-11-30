#!/usr/bin/python3
""" Script that lists all cities from the database """

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = database.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities \
             INNER JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    database.close()
