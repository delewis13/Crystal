from flask import Flask
from flask import request
from flask import send_from_directory
from WordEmb2 import WordEmbedder
from personality_predicter import predict_personality_from_post as predict
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def init():
    return 'Welcome'


@app.route('/api/<long_string>', methods = ['POST'])
def predict(long_string):
	# ---- Loading the classifier ---
	# print('[+] Loading model!');
	# print();
    classifier = pickle.load(open('xgboost_model.pickle','rb'))
    prediction = predict(classifier, long_string, wb)


    return prediction

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
