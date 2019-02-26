import pickle
from flask import Flask, render_template
from flask_cors import CORS
from flask import request
from flask import send_from_directory
from WordEmb2 import WordEmbedder
import pickle
import personality_predicter
app = Flask(__name__)
# cross origin resource sharing
cors = CORS(app)


@app.route('/', methods=['GET'])
def init():
  return 'Welcome'


@app.route('/crystal', methods=['GET'])
def crystal():
  return render_template('index.html')


@app.route('/api/<long_string>', methods=['POST', 'GET'])
def predict(long_string):
  wb = WordEmbedder(embedding_index='./embeddings_index.pickle')
  # ---- Loading the classifier ---
  # print('[+] Loading model!');
  # print();
  print(long_string)
  classifier = pickle.load(open('xgboost_model.pickle', 'rb'))
  prediction = personality_predicter.predict_personality_from_post(classifier, long_string, wb)

  print(prediction)

  return prediction


if __name__ == '__main__':
  #app.run(host='0.0.0.0', debug=True)
  app.run(host='0.0.0.0', ssl_context=('cert.pem', 'key.pem'))
  #app.run()
