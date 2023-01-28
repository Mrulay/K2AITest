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
            content['data'][0]['actions'] = [{'action': 'xx', 'actionId': 'xx'}, 
                                        {'action': 'xx', 'actionId': 'xx'},
                                        {'action': 'xx', 'actionId': 'xx'},
                                        {'action': 'xx', 'actionId': 'xx'}, 
                                        {'action': 'xx', 'actionId': 'xx'}]
            print(content)
            return content
        else:
            resList = []
            resDict ={}
            for i in range(0,5):
                resDict['action'] = data[res[i]]
                resDict['actionId'] = res[i] 
                resList.append(resDict)
                resDict = {}
            content['data'][0]['actions'] = resList
            print(content)
            return content
    except KeyError:
        return 'Input does not exist in the data'
