import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="coffee_machine_management"
)

my_cursor = mydb.cursor()
