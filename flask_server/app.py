from flask import Flask
from flask import request
from flask import send_from_directory
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def init():
    return 'Welcome'


@app.route('/long_string', methods = ['POST'])
def predict():


    return

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
