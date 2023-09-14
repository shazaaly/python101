#!/usr/bin/python3
import MySQLdb
MY_HOST = 'localhost'
MY_USER = 'root'
MY_PASS = 'tormtorm'
MY_DB = 'mydb'

# Define the list of employees
employees = ["Shaza", "Hussien", "Ibrahim", "Dany"]

db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
cur = db.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS employees(id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,\
        title TEXT NOT NULL)")

# Insert data into the "employees" table
for emp in employees:
    cur.execute("INSERT INTO employees(title) VALUES(%s)", (emp,))

# Commit the changes to the database
db.commit()

# Query and display the inserted data
cur.execute("SELECT * FROM employees")
result = cur.fetchall()

for row in result:
    print(row)

# Close the cursor and database connection
cur.close()
db.close()
