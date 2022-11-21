import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    arg = request.args['arg1']
    try: 
        return arg
    except KeyError:
        return 'Input does not exist in the data' 