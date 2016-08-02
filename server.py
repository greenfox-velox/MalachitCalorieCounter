from flask import Flask, render_template, jsonify, request, json
app = Flask(__name__)

meal_list = [{'id': 13, 'text': 'Krumpli', 'calories': 300, 'date': '2016-01-01'},
    {'id': 14, 'text': 'Kacsa', 'calories': 400, 'date': '2016-02-02'},
    {'id': 15, 'text': 'Beka', 'calories': 200, 'date': '2016-08-01'}]

@app.route("/")
def index():
    return render_template('index.html')

# This should be integrated to the master, the returns must be the DB results
@app.route("/list", methods=['GET', 'POST', 'DELETE', 'PUT'])
def list_all():
    if request.method == 'GET':
      return jsonify(meal_list)
    elif request.method == 'POST':
      meal_list.append(request.json)
      return jsonify(meal_list)
    elif request.method == 'DELETE':
      pass
      # DELETE record from DB
    else:
      pass
      # UPDATE record in DB

# Getting the filter parameter trough anchor in the URL, in this case the date
# This is just the showcase on the mock meal_list
@app.route("/filter", methods=['GET'])
def filter_list():
    #Change this line for the proper DB query using request.args.get('key')
    response = list(filter((lambda elem: elem['date'] == request.args.get('date')), meal_list))
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=3000)
