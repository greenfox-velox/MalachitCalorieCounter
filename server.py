from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
from sqlquery import *
import os

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/list", methods=['GET'])
def foods():
  return jsonify(get_all())

@app.route("/list", methods=['POST'])
def add_foods():
  add_meal()
  return foods()
  # return jsonify([request.json])

@app.route("/list", methods=['DELETE'])
def del_food():
  del_meal()
  return foods()


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 3000))
  app.run(debug=True, host='localhost', port=port)
