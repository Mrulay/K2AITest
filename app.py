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
        content['data'][0]['actions'] = [{'action': 'Apply for Affordable Buss Pass', 'actionId': 'a1o4t00000000i8AAA'}, 
                                        {'action': 'Apply for an Ontario drivers licence', 'actionId': 'a1o4t00000000CRAAY'},
                                        {'action': 'Get a map of the city and a bus schedule - apps ?', 'actionId': 'a1o4t00000000CSAAY'},
                                        {'action': 'Learn about public transportation options available to me', 'actionId': 'a1o4t00000000CQAAY'}, 
                                        {'action': 'Learn more about alternative transport , car rental', 'actionId': 'a1o4t00000000aQAAQ'}]
        return content
#         if len(res)==0:
#            content['data'][0]['actions'] = [{'action': 'xx', 'actionId': 'xx'}, 
#                                        {'action': 'xx', 'actionId': 'xx'},
#                                         {'action': 'xx', 'actionId': 'xx'},
#                                         {'action': 'xx', 'actionId': 'xx'}, 
#                                         {'action': 'xx', 'actionId': 'xx'}]
#             print(content)
#             return content
#         else:
#             resList = []
#             resDict ={}
#             for i in range(0,5):
#                 resDict['action'] = data[res[i]]
#                 resDict['actionId'] = res[i] 
#                 resList.append(resDict)
#                 resDict = {}
#             content['data'][0]['actions'] = resList
#             print(content)
#             return content
#     except KeyError:
#         return 'Input does not exist in the data'
