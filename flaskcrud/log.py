from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'        
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flaskapp'
                
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userdetails = request.form
        name = userdetails['name']
        email = userdetails['email']
        cur = mysql.connection.cursor()
        cur.execute("insert into users(name, email) VALUES(%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()
        return redirect('/login')
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        logindetails = request.form
        name = logindetails['name']
        email = logindetails['email']
        cur = mysql.connection.cursor()
        sql = "select * from users WHERE name=%s AND email=%s"
        cur.execute(sql, (name, email))
        result = cur.fetchone()
        mysql.connection.commit()
        cur.close()

        if result:
            return '<h1>LOGIN IS SUCESSFULL</h1>'
        else:
            return redirect('/')

    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=3000)
