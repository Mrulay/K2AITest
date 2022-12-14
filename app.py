import flask
import re 
import json
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from flask import request

app = flask.Flask(__name__)

wordVectors = KeyedVectors.load(r'w2v.wordvectors')
f = open(r'data.json')
data = json.load(f)

@app.route('/', methods=['POST'])
def home():
    content = request.data
    print(content)
    my_json = content.decode('utf8')
    print(my_json)
    content = json.loads(my_json)
    print(content['data'])
    try: 
        #prediction will happen based on the 'responseID'
        preds = wordVectors.most_similar(content['data'][0]['responseId'], [], 5341)
        preds = [item[0] for item in preds]
        res = []
        for num, i in enumerate(preds):
            if i[2] == 'o':
                res.append(i)
        if len(res)==0:
            content['data'][0]['actionId'] = 'xx'
            content['data'][0]['action'] = 'xx'
            print(content)
            return content
        else:
            content['data'][0]['actionId'] = res[0]
            content['data'][0]['action'] = data[res[0]]
            print(content)
            return content
    except KeyError:
        return 'Input does not exist in the data'
