import mysql.connector
import credentials as cd


mydb = mysql.connector.connect(
    host=cd.host,
    user = cd.user,
    password= cd.password,
    port = cd.port
)

data = mydb.cursor()

data.execute("show databases")

for i in data:
    print(i)


