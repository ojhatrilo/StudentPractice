import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  port="3309",
  password="Admin@123",
  database="ojha"
)
mycur=mydb.cursor()
mycur.execute("CREATE TABLE Registration (id int(1), fname VARCHAR(255),age INT(2))")
print("Table names is sucssessfully done")

sql = "INSERT INTO Registration(id,fname,age) VALUES (%s, %s, %s)"
val = (1,"Ansu",31)

mycur.execute(sql, val)

mydb.commit()

print(mycur.rowcount, "record inserted")

