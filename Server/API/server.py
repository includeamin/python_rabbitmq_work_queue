from flask import Flask,request
from flask_cors import CORS
from Bridges.RabbitMq import connection

app = Flask(__name__)
CORS(app)

@app.route('/task/assign')
def  new_task():
    pass
@app.route('/task/checkout/<id>')
def checkout(id):
    pass
