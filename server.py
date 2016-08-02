from flask import Flask, render_template, jsonify
app = Flask(__name__)



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/list", methods=['GET'])
def get_all_food():
    return jsonify([{'id': 13, 'text': 'Krumpli', 'calories': 300, 'date': '2016-01-01'},
    {'id': 14, 'text': 'Kacsa', 'calories': 400, 'date': '2016-02-02'},
    {'id': 15, 'text': 'Beka', 'calories': 200, 'date': '2016-08-01'}])

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=3000)
