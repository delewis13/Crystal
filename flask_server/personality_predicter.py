# --- libs ---
from WordEmb2 import WordEmbedder
from data_parser import DataParser
import sklearn

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import metrics
import pickle
import numpy as np

from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

import preprocessor as p

import argparse

# --- Classifier ---
personality_types = ['INFJ', 'ENTP', 'INTP', 'INTJ', 'ENTJ', 'ENFJ', 'INFP', 'ENFP',
					'ISFP', 'ISTP', 'ISFJ', 'ISTJ', 'ESTP', 'ESFP', 'ESTJ', 'ESFJ'];
#

def predict_personality_from_post(model, post, wb):
	# Encoder
	encoder = LabelEncoder();
	encoder.classes_ = np.load('classes.npy');

	# Preprocess the tweets
	post = p.tokenize(post);
	#print(post);

	# Grab the embeddings and averages
	embeddings_from_post = np.array(wb.compute_embeddings([post], wb.embedding_index));
	embedding_avgs = wb.compute_average(embeddings_from_post);

	#print('[+] Embedding length from test text: ' + str(len(embeddings_from_post)));
	#print(wb.compute_average(embeddings_from_post).shape);
	#print('[+] Prediction: ');

	# Compute the prediction
	prediction = model.predict(embedding_avgs);
	#print(prediction);

	# Get personality type
	index_personality = prediction[0] - 1;
	personality_type = personality_types[index_personality];

	prediction = [prediction[0] - 1];
	personality_type = encoder.inverse_transform(prediction)[0];


	return personality_type;



# --- Good ol main ---
def main():
	# --- Arg parser ---
	parser = argparse.ArgumentParser();
	parser.add_argument("message", help="Post to predict personality");
	args = parser.parse_args();

	post = args.message;
	#print(post);


	# --- Word embeddings ---
	# word embeddings
	wb = WordEmbedder(embedding_index='./embeddings_index.pickle');


	# ---- Loading the classifier ---
	# print('[+] Loading model!');
	# print();
	classifier = pickle.load(open('xgboost_model.pickle','rb'));

	# --- Predicting personality ---
	personality_type = predict_personality_from_post(classifier, post, wb);
	print(personality_type);



	return;


if __name__ == "__main__":
	main();
