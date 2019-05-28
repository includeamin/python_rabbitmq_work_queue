from flask import Flask,request,jsonify
from flask_cors import CORS
from Bridges.RabbitMq import connection

app = Flask(__name__)
CORS(app)

@app.route('/task/assign')
def  new_task():
    try:
        pass
    except Exception as ex:
        return jsonify({"State":False,"Description":ex.args})
@app.route('/task/checkout/<id>')
def checkout(id):
    try:
        pass
    except Exception as ex:
        return jsonify({"State":False,"Description":ex.args})




if __name__ == "__main__":
    app.run(host="0.0.0.0",port='3000',debug=True)