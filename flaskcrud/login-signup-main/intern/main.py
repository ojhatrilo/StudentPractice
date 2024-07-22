from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flash messages

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    port = '3306',
    database="signup"
)
mycursor = mydb.cursor()

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        sql = "SELECT * FROM signupdet WHERE username = %s AND passwrd = %s"
        values = (username, password)
        mycursor.execute(sql, values)
        result = mycursor.fetchone()
        if result:
            # User exists, redirect to dashboard
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            # User does not exist, show an error message
            flash("Invalid username or password")
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/about', methods=["GET", "POST"])
def about():
    return render_template('bg.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        return "Logged in successfully!!! Welcome, {}".format(username)
    else:
        return redirect(url_for('index'))

@app.route('/signup', methods=["GET", "POST"])
def sgn():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Use parameterized query with placeholders
        sql = "INSERT INTO signupdet (username, passwrd) VALUES (%s, %s)"
        values = (username, password)
        # Execute query with parameters
        mycursor.execute(sql, values)
        # Commit changes to the database
        mydb.commit()
        # Store user info in session and redirect to dashboard
        session['username'] = username
        return redirect(url_for('dashboard'))
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
