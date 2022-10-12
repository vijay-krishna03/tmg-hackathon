from flask import Flask,render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask import request
from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'geeklogin'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login', methods = ['POST', 'GET'])
def login():
        return render_template('PG2-doc.html')

@app.route('/login2', methods = ['POST', 'GET'])
def login2():
        return render_template('PG2-patient.html')

@app.route('/doctor', methods = ['POST', 'GET'])
def doctor():
 if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			session['id'] = account['id']
			session['username'] = account['username']
			msg = 'Logged in successfully !'
			return render_template('doctor.html', msg = msg)
		else:
			msg = 'Incorrect username / password !'
 return render_template('PG2-doc.html', msg = msg)

@app.route('/access', methods = ['POST', 'GET'])
def access():
        return render_template('enter_view.html')

@app.route('/sub', methods = ['POST', 'GET'])
def sub():
        return render_template('submit.html')

@app.route('/docu', methods = ['POST', 'GET'])
def docu():
        if request.method == 'POST' and 'patient_id' in request.form and 'password' in request.form and 'phoneno' in request.form:
            return render_template('documents.html')
        else:

            return render_template('PG2-patient.html')

@app.route('/viewu', methods = ['POST', 'GET'])
def viewu():
        if request.method == 'POST' and 'filename' in request.form and 'file' in request.form :
            return render_template('documents.html')
        else:
            return render_template('submit.html')
@app.route('/register', methods = ['POST', 'GET'])
def register():
        return render_template('reg.html')

@app.route('/signin')
def signin():
    return render_template('index.html')

@app.route('/plswork',methods = ['POST', 'GET'])
def plswork():
    if request.method == 'POST':
            return render_template('documents.html')


if __name__ == '__main__':
    app.run(debug=True)
