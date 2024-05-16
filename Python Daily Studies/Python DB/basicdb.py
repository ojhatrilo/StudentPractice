import mysql.connector

connect = mysql.connector.connect(
    host="localhost",
    username = 'root',
    password = 'root',
    port = "3306",
    database = 'demo'
)

cursor = connect.cursor()
# cursor.execute("CREATE DATABASE IF NOT EXISTS demo")
# cursor.execute("CREATE TABLE IF NOT EXISTS students(id INT auto_increment primary key, name varchar(255),password varchar(255))")

cursor.execute("INSERT INTO students(name,password) VALUES('saurabh','1234')")

connect.commit()
print("inserted Sucefully")




