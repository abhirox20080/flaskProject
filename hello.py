from flask import Flask
import flask
#from flask import render_templates
app = Flask(__name__)

@app.route('/')
def hello_world():
    return flask.render_template('hello.html')

if __name__ == '__main__':
    app.debug = True
    app.run()