import flask
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from flask import request

app = flask.Flask(__name__)

wordVectors = KeyedVectors.load('w2v.wordvectors')

@app.route('/', methods=['GET'])
def home():
    arg = request.args['arg1']
    try: 
        preds = wordVectors.most_similar(arg)
        preds = [item[0] for item in preds]
        res = []
        for num, i in enumerate(preds):
            if i[2] == 'o':
                res.append(i)
        return res
    except KeyError:
        return 'Input does not exist in the data' 
