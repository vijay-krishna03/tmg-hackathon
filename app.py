#
# from flask import Flask,render_template,request
# from flask_mysqldb import MySQL
# from flaskext.mysql import MySQL
#
#
# app = Flask(__name__)
#
# app.config['MYSQL_HOST'] = '192.168.0.108'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'flask'
# mysql = MySQL()
# mysql.init_app(app)
# cursor=mysql.get_db().cursor()
#
# @app.route('/')
# def index():
#     return render_template('index.html')
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
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask,render_template, request
# from flask_mysqldb import MySQL
#
# app = Flask(__name__)
#
# app.config['MYSQL_HOST'] = 'localhost'
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
#  if __name__ == '__main__':
#      app.run(debug=True)
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
