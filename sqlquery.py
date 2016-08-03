from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'almafa'
app.config['MYSQL_DB'] = 'FoodCalories'
mysql = MySQL(app)

def get_all ():
  list_w_key = []
  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM Foods;')
  rv = cur.fetchall()
  for item in rv:
    i = {
      'id':item[0],
      'name':item[1],
      'calories':item[2],
      'date':item[3]
        }
    list_w_key.append(i)
  return list_w_key

def add_meal():
  query = 'INSERT INTO Foods (name, calories, date) VALUE (%s, %s, %s);'
  values = ('papaja', 20, '2016-05-18')
  cur = mysql.connection.cursor()
  cur.execute(query, values)
  mysql.connection.commit()
