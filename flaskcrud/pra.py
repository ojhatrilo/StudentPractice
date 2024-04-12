
# from flask_mysqldb import MySQL

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="Admin@123",
  database = "elakiya"
)

mycursor = mydb.cursor() 
# mycursor.execute("SHOW DATABASES") 
# mycursor.execute("create database elakiya")

# mycursor.execute("create table student (name varchar(255), address varchar(255))")
# sql = "INSERT INTO student (name, address) VALUES (%s, %s)"
# val = [
    
#  ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')

# ]
# # #
# mycursor.executemany(sql,val)


mycursor.execute("SELECT * FROM student where name = 'Amy' and address = 'Apple st 652' ")

myresult = mycursor.fetchone()

for x in myresult:
  print(x)




# mydb.commit()
# for x in mycursor:
#     print(x)