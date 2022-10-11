#
# from flask import Flask,render_template,request
# from flask_mysqldb import MySQL
#
#
# app = Flask(__name__)
# app.config['MYSQL_UNIX_SOCKET'] = 'TCP'
# app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'hospital'
# mysql = MySQL(app)
# @app.route('/')
# def index():
#     return render_template('form.html')
#
# @app.route('/login', methods = ['POST', 'GET'])
# def login():
#     if request.method == 'GET':
#         return "Login via the login Form"
#
#     if request.method == 'POST':
#         name = request.form['name']
#         age = request.form['age']
#         cursor = mysql.connection.cursor()
#         cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,age))
#         mysql.connection.commit()
#         cursor.close()
#         return f"Done!!"
# if __name__ == '__main__':
#      app.run(debug=True)
#
# app.run(host='localhost', port=5000)


# from flask import Flask,render_template, request
# from flask_mysqldb import MySQL
#
# app = Flask(__name__)
# app.config['MYSQL_UNIX_SOCKET'] = 'TCP'
# app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'hospital'
#
# mysql = MySQL(app)
#
# @app.route('/form')
# def form():
#     return render_template('form.html')
#
# @app.route('/login', methods = ['POST', 'GET'])
# def login():
#     if request.method == 'GET':
#         return "Login via the login Form"
#
#     if request.method == 'POST':
#         name = request.form['name']
#         age = request.form['age']
#         cursor = mysql.connection.cursor()
#         cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,age))
#         mysql.connection.commit()
#         cursor.close()
#         return f"Done!!"
#
# app.run(host='localhost', port=5000)
 # if __name__ == '__main__':
 #     app.run(debug=True)
from flask import Flask,render_template

app = Flask(__name__)

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
        return render_template('doctor.html')

if __name__ == '__main__':
    app.run(debug=True)
