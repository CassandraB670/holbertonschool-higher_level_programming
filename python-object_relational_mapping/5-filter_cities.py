#!/usr/bin/python3
""" Script that takes in the name of a state as an argument
and lists all cities of the state, using the database """

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = database.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name FROM cities \
             INNER JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s \
                ORDER BY cities.id ASC", [state_name])
    rows = cursor.fetchall()
    index = []

    for row in rows:
        index.append(row[1])
    print(", ".join(index))

    cursor.close()
    database.close()
