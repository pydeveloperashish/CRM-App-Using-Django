# Run 'python mydb.py' to create the database.

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost', 
    user = 'root',
    passwd = 'admin12345'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a dataBase
cursorObject.execute("CREATE DATABASE dcrm")

print("All Done!")