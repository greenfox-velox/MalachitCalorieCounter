from flask import Flask, render_template, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'almafa'
app.config['MYSQL_DB'] = 'FoodCalories'
mysql = MySQL(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get")
def foods():
    list_w_key = []
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Foods')
    rv = cur.fetchall()
    for item in rv:
        i = {
            'id':item[0],
            'name':item[1],
            'calories':item[2],
            'date':item[3]
        }
        list_w_key.append(i)
    return jsonify(list_w_key)


if __name__ == "__main__":
    app.run(debug=True, host='localhost')
