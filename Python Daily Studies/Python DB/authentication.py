import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    port = "3306",
    database = "authentication"
)

db = mydb.cursor()
# db.execute ("create database if not exists authentication")
db.execute("create table if not exists userdata (username varchar(255) not null, password varchar(255) not null)")

def register():
    username = input("enter your name:")
    password = input("create your password:")
    password1 = input("confirm your password:")
    if password == password1:
        sql = "insert into userdata (username,password) values(%s,%s)"
        value = (username,password)
        db.execute(sql,value)
        mydb.commit()
        print("Successfully registered")
        
    else:
        print("password not match")


def login():
    username = input("enter your name:")
    password = input("create your password:")

    sql = "select * from userdata where username=%s and password =%s"
    value = (username,password)
    db.execute(sql,value)
    result = db.fetchone()
    # print(result)

    if result:
        print("You are sucefully logedin")
        print("Welcome to the class")
    else:
        print("incorect username and password")

while True:
    options = input("option 1-register\noption 2-login:")
    if options == "1":
        register()
    elif options == "2":
        login()
        break
    else:
        break






