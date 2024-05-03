import mysql.connector
import credentials as cd


mydb = mysql.connector.connect(
    host=cd.host,
    user = cd.user,
    password= cd.password,
    port = cd.port
)

data = mydb.cursor()

# data.execute("show databases")
#
# for i in data:
#     print(i)

# point = mydb.cursor()
# point.execute("show databases")

# sql = "create database if not exists soni"
# sql = "create table if not exists data (name varchar(255), age INT, DOB Date )"

# sql = "insert into data (name,age,DOB) VALUES (%s,%s,%s)"
# val = [("somiya",21,'2002-04-05'),
#        ("nithiya",24,'2000-01-30')
#        ]

# sql = "select * from data"
# point.execute(sql)
# for i in point:
#     print(i)



# for i in point:
#     print(i)

