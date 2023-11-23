Task 0 - My privileges!
    File 0-privileges.sql

Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

Task 1 - Root user
    File 1-create_user.sql

Write a script that creates the MySQL server user user_0d_1.

    user_0d_1 should have all privileges on your MySQL server
    The user_0d_1 password should be set to user_0d_1_pwd
    If the user user_0d_1 already exists, your script should not fail

Task 2 - Read user
    File 2-create_read_user.sql

Write a script that creates the database hbtn_0d_2 and the user user_0d_2.

    user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
    The user_0d_2 password should be set to user_0d_2_pwd
    If the database hbtn_0d_2 already exists, your script should not fail
    If the user user_0d_2 already exists, your script should not fail

Task 3 - Always a name
    File 3-force_name.sql

Write a script that creates the table force_name on your MySQL server.

    force_name description:
        id INT
        name VARCHAR(256) can’t be null
    The database name will be passed as an argument of the mysql command
    If the table force_name already exists, your script should not fail

Task 4 - ID can't be null
    File 4-never_empty.sql

Write a script that creates the table id_not_null on your MySQL server.

    id_not_null description:
        id INT with the default value 1
        name VARCHAR(256)
    The database name will be passed as an argument of the mysql command
    If the table id_not_null already exists, your script should not fail

Task 5 - Unique ID
    File 5-unique_id.sql

Write a script that creates the table unique_id on your MySQL server.

    unique_id description:
        id INT with the default value 1 and must be unique
        name VARCHAR(256)
    The database name will be passed as an argument of the mysql command
    If the table unique_id already exists, your script should not fail
