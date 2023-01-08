import flask
import re 
import json
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from flask import request

app = flask.Flask(__name__)

wordVectors = KeyedVectors.load(r'w2v.wordvectors')

@app.route('/', methods=['POST'])
def home():
    content = request.data
    #content = str(content)
    content = content.decode('UTF-8')
    content = content[20:-10].rstrip()
    content = re.sub(r'\r\n', '', content)
    content = content.replace("\'", "\"")
    #print(content)
    content = json.loads(content)
    #print(type(content["responseId"]))
    try: 
        #prediction will happen based on the 'responseID'
        preds = wordVectors.most_similar(content['responseId'], [], 5341)
        preds = [item[0] for item in preds]
        res = []
        for num, i in enumerate(preds):
            if i[2] == 'o':
                res.append(i)
        if len(res)==0:
            content['ActionId'] = 'xx'
            return content
        else:
            content['ActionId'] = res[0]
        return content
    except KeyError:
        return 'Input does not exist in the data'
