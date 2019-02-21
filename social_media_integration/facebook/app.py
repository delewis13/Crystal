import os
import json
from flask_bootstrap import Bootstrap
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from logzero import logger

acceleration = {}

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    return app

app = create_app()

# cross origin resource sharing
cors = CORS(app)

def before_request():
    app.jinja_env.cache = {}

# show index html page
@app.route('/', methods=['GET'])
def index():

    return render_template('main.html')

# show index html page
@app.route('/logout', methods=['GET'])
def logout():

    return render_template('main.html')

if __name__ == '__main__':
    app.before_request(before_request)
    app.run(host='0.0.0.0', debug=True, port=5000)
