import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="localhost",
        port=3306,
        database="intern_task"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
cur.execute(
    "SELECT * FROM student WHERE username=?", 
    ('andrew',))

for each in cur:
    print('name',each[0])
    # print(f"First Name: {first_name}, Last Name: {last_name}")