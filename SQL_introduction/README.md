Task 0 - List databases
    File 0-list_databases.sql

Write a script that lists all databases of your MySQL server.

Task 1 - Create a database
    File 1-create_database_if_missing.sql

Write a script that creates the database hbtn_0c_0 in your MySQL server.

    If the database hbtn_0c_0 already exists, your script should not fail
    You are not allowed to use the SELECT or SHOW statements

Task 2 - Delete a database
    File 2-remove_database.sql

Write a script that deletes the database hbtn_0c_0 in your MySQL server.

    If the database hbtn_0c_0 doesn’t exist, your script should not fail
    You are not allowed to use the SELECT or SHOW statements

Task 3 - List tables
    File 3-list_tables.sql

Write a script that lists all the tables of a database in your MySQL server.

    The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)

Task 4 - First table
    File 4-first_table.sql

Write a script that creates a table called first_table in the current database in your MySQL server.

    first_table description:
        id INT
        name VARCHAR(256)
    The database name will be passed as an argument of the mysql command
    If the table first_table already exists, your script should not fail
    You are not allowed to use the SELECT or SHOW statements

Task 5 - Full description
    File 5-full_table.sql

Write a script that prints the following description of the table first_table from the database hbtn_0c_0 in your MySQL server.

    The database name will be passed as an argument of the mysql command
    You are not allowed to use the DESCRIBE or EXPLAIN statements

Task 6 - List all in table
    File 6-list_values.sql

Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

    All fields should be printed
    The database name will be passed as an argument of the mysql command

Task 7 - First add
    File 7-insert_value.sql

Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

    New row:
        id = 89
        name = Best School
    The database name will be passed as an argument of the mysql command

Task 8 - Count 89
    File 8-count_89.sql

Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

    The database name will be passed as an argument of the mysql command

Task 9 - Full creation
    File 9-full_creation.sql

Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

    second_table description:
        id INT
        name VARCHAR(256)
        score INT
    The database name will be passed as an argument to the mysql command
    If the table second_table already exists, your script should not fail
    You are not allowed to use the SELECT and SHOW statements
    Your script should create these records:
        id = 1, name = “John”, score = 10
        id = 2, name = “Alex”, score = 3
        id = 3, name = “Bob”, score = 14
        id = 4, name = “George”, score = 8

Task 10 - List by best
    File 10-top_score.sql

Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

    Results should display both the score and the name (in this order)
    Records should be ordered by score (top first)
    The database name will be passed as an argument of the mysql command

Task 11 - Select the best
    File 11-best_score.sql

Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

    Results should display both the score and the name (in this order)
    Records should be ordered by score (top first)
    The database name will be passed as an argument of the mysql command

Task 12 - Cheating is bad
    File 12-no_cheating.sql

Write a script that updates the score of Bob to 10 in the table second_table.

    You are not allowed to use Bob’s id value, only the name field
    The database name will be passed as an argument of the mysql command

Task 13 - Score too low
    File 13-change_class.sql

Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

    The database name will be passed as an argument of the mysql command

