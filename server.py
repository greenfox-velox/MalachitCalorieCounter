from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

meal_list = [{'id': 13, 'text': 'Krumpli', 'calories': 300, 'date': '2016-01-01'},
    {'id': 14, 'text': 'Kacsa', 'calories': 400, 'date': '2016-02-02'},
    {'id': 15, 'text': 'Beka', 'calories': 200, 'date': '2016-08-01'}]

ok_status = [{'status': 'OK'}]

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/list", methods=['GET'])
def get_all_food():
    return jsonify(meal_list)

@app.route("/list", methods=['POST'])
def add_new_food():
    meal_list.append({'id': 100, 'text': 'TEST MEAL', 'calories': 100, 'date': '2016-01-01'})
    print(meal_list)
    return jsonify(ok_status)

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=3000)
