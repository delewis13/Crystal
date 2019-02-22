#from keras.preprocessing.text import Tokenizer
#from keras.preprocessing.sequence import pad_sequences
import pandas as pd
import numpy as np
import os

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

import pickle
from nltk.corpus import wordnet
from nltk.tokenize import TreebankWordTokenizer

# FOR REPEATABLITY
#RANDOM_SEED = 7;
#np.random.seed(RANDOM_SEED);

class WordEmbedder:
	def __init__(self, embedding_index=None):
		self.label_encoder = LabelEncoder();
		self.embedding_index = embedding_index;
		self.embedding_dims = 25;
		return;

	# get training and test data from pickle (saves computation time)
	def prep_data_from_pickle(self, data_pkl, label_pkl, VALIDATION_SPLIT=0.2):
		# Load the pickles
		data = pickle.load(open(data_pkl, "rb"));
		labels = pickle.load(open(label_pkl, "rb"));

		print('[+] Shape of data tensor: {}'.format(data.shape));
		print('[+] Shape of label tensor: {}'.format(labels.shape));

		# split the data into a training set and a validation set
		indices = np.arange(data.shape[0])
		np.random.shuffle(indices)
		data = data[indices]
		labels = labels[indices]
		nb_validation_samples = int(VALIDATION_SPLIT * data.shape[0])


		x_train = data[:-nb_validation_samples]
		y_train = labels[:-nb_validation_samples]
		x_val = data[-nb_validation_samples:]
		y_val = labels[-nb_validation_samples:]

		return (x_train, y_train, x_val, y_val);




	# prepare text data from csv file
	def prepare_text_data(self, csv_file, VALIDATION_SPLIT=0.2):
		df = pd.read_csv(csv_file, delimiter=',');

		# For computation save
		#df = df.head(n=10);

		# Randomly sample 70% of your dataframe
		#df = df.sample(frac=0.7)

		# Randomly sample 7 elements from your dataframe
		#df = df.sample(n=7)

		# --- Prepare the texts ---
		# Get the texts
		texts = df['post'].tolist();



		# Compute the embedding index if none is supplied
		if self.embedding_index == None:
			embedding_index = self.compute_embedding_dictionary();
		else:
			print('[+] Unloading pickle ' + str(self.embedding_index))
			embedding_index = pickle.load(open(self.embedding_index, "rb"));

		# Compute the embeddings
		print('[+] Computing the embeddings');
		embeddings = self.compute_embeddings(texts, embedding_index);


		# Hacky solution
		self.embeddings_index = embedding_index;

		tokenizer = TreebankWordTokenizer();

		# DEBUG
		'''
		print(embeddings[0]);
		print(len(embeddings[20]));
		print(texts[20])
		print(tokenizer.tokenize(texts[20]))
		print(embedding_index['well'])
		'''
		embeddings = np.array(embeddings);
		#print(embeddings.shape);

		# The data will be the embedding averages
		print('[+] Computing the embedding averages');
		data = self.compute_average(embeddings);
	
		# --- Create one hot encoding for outputs ---
		print('[+] One hot encoding the labels')
		personality_df = df['type'];
		labels = np.array(self.one_hot_encode(personality_df));



		# --- split into train and validation set ---
		print('[+] Shape of data tensor: {}'.format(data.shape));
		print('[+] Shape of label tensor: {}'.format(labels.shape));

		# Pickilizing vectorized data
		print('[!] Pickilizing vectorized data');
		pickle.dump(data, open('data.pickle', 'wb'));
		print('[!] Pickilizing vectorized labels');
		pickle.dump(labels, open('labels.pickle', 'wb'));


		# split the data into a training set and a validation set
		indices = np.arange(data.shape[0])
		np.random.shuffle(indices)
		data = data[indices]
		labels = labels[indices]
		nb_validation_samples = int(VALIDATION_SPLIT * data.shape[0])


		x_train = data[:-nb_validation_samples]
		y_train = labels[:-nb_validation_samples]
		x_val = data[-nb_validation_samples:]
		y_val = labels[-nb_validation_samples:]


		return (x_train, y_train, x_val, y_val);




	# return averages for each sentence embedding
	def compute_average(self, embeddings):
		mean_matrix = np.zeros((embeddings.shape[0], self.embedding_dims))
		#print('[+] mean matrix: ' + str(mean_matrix.shape));
		for i in range(embeddings.shape[0]):
			mean_matrix[i,:] = np.mean(embeddings[i], axis=0);
			#print(embeddings[i]);
			#print(mean);
		return mean_matrix;

	# compute embeddings given a list of texts
	def compute_embeddings(self, texts, embedding_index):
		tokenizer = TreebankWordTokenizer();
		embeddings = [];

		for text in texts:
			embedding = [];

			for word in tokenizer.tokenize(text):
				word_embedding = self.compute_word_embedding(word, embedding_index);
				if word_embedding is not None:
					embedding.append(np.array(word_embedding));
				else:
					# pad with 0s
					zero_arr = np.zeros(25,);
					embedding.append(zero_arr);
					continue;

			embeddings.append(embedding);
		return embeddings;

	# compute embedding from word using the glove
	def compute_word_embedding(self, word, embedding_index):
		word = word.lower();
		try:
			return embedding_index[word];
		except:
			return None;


 
	def compute_embedding_dictionary(self):
		# Load the whole embedding matrix
		embeddings_index = {}
		with open('./glove/glove.twitter.27B.25d.txt', encoding='utf-8') as f:
			for line in f:
				values = line.split()
				word = values[0]

				if wordnet.synsets(word):
					embed = np.array(values[1:], dtype=np.float32)
					embeddings_index[word] = embed
					print(word);

		# save the embeddings
		pickle.dump(embeddings_index, open('embeddings_index.pickle', 'wb'));

		return embeddings_index;

	# --- Helper function ---
	# returns a numpy array of one hot encoded output
	def one_hot_encode(self, data_df):
		# Integer encode
		integer_encoded = self.label_encoder.fit_transform(data_df);
		#print(integer_encoded);

		# Binary encode
		onehot_encoder = OneHotEncoder(sparse=False);
		integer_encoded = integer_encoded.reshape(len(integer_encoded), 1);
		onehot_encoded = onehot_encoder.fit_transform(integer_encoded);
		#print(onehot_encoded[0,:])

		return onehot_encoded;

	# Invert the labels
	def get_personality_from_encoding(self, onehot_encoded):
		inverted = [];
		for i in range(onehot_encoded.shape[0]):
			inverted.append(self.label_encoder.inverse_transform([np.argmax(onehot_encoded[i, :])]));
		return inverted;



if __name__ == "__main__":
	wb = WordEmbedder(embedding_index='./embeddings_index.pickle');
	#wb = WordEmbedder();

	preprocessed_data = "./Dataset/clean_mbti.csv";
	wb.prepare_text_data(preprocessed_data);