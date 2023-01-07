import flask
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from flask import request

app = flask.Flask(__name__)

wordVectors = KeyedVectors.load(r'w2v.wordvectors')

@app.route('/', methods=['GET'])
def home():
    content = request.get_json()
    try: 
        #prediction will happen based on the 'responseID'
        preds = wordVectors.most_similar(content['responseId'], [], 5341)
        preds = [item[0] for item in preds]
        res = []
        for num, i in enumerate(preds):
            if i[2] == 'o':
                res.append(i)
        if len(res)==0:
            content['ActionID'] = 'xx'
            return content
            #content['Action'] = 'AI Failed to predict'
        else:
            content['ActionID'] = res[0]
            return content
    except KeyError:
        return 'Input does not exist in the data' 
