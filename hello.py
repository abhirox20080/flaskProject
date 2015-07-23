from flask import Flask
import flask
import os
import json
import bson

from bson import json_util

import pymongo
#from pymongo import json_utils
from bson import Binary, Code
#from pymongo import json_util
#from flask import render_templates
app = Flask(__name__)
# setting up template directory
#ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '/static/')

#app = Flask(__name__, template_folder=ASSETS_DIR, static_folder=ASSETS_DIR)

@app.route('/')
def hello_world():
    return flask.render_template('index.html')

@app.route('/db')
def DbHandler():
    client = pymongo.MongoClient('localhost', 27017)
    db = client['mydb']
    collection = db['mycollection']
    data=collection.find_one()
    print "Fetching data"
    print data
    x=json_util.dumps(data)
#    x = json.loads(json_util.dumps(data))
    print type(x)
    return(x)

if __name__ == '__main__':
#    app.debug = True
    app.run(port=9090 , host='0.0.0.0', debug=True)