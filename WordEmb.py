from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pandas as pd
import numpy as np
import os

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from keras.layers import Embedding

class WordEmbedder:
	def __init__(self, glove_dir, MAX_NB_WORDS=1000, MAX_SEQUENCE_LENGTH=10, EMBEDDING_DIM=100):
		self.GLOVE_DIR = glove_dir;
		self.MAX_NB_WORDS = MAX_NB_WORDS;
		self.MAX_SEQUENCE_LENGTH = MAX_SEQUENCE_LENGTH;
		self.EMBEDDING_DIM = EMBEDDING_DIM;
		self.label_encoder = LabelEncoder();
		return;


	def prepare_text_data_2(self, csv_file, VALIDATION_SPLIT=0.2):
		df = pd.read_csv(csv_file, delimiter=',');

		# For computation save
		df = df.tail(n=10);
		# --- Prepare the texts ---
		texts = df['post'].tolist();

		self.compute_embeddings(texts);


		# --- Create one hot encoding for outputs ---
		personality_df = df['type'];

		labels = np.array(self.one_hot_encode(personality_df));


		return;

	# compute embeddings given a list of texts
	def compute_embeddings(self, texts):
		# compute the embedding dictionary first
		self.compute_embedding_dictionary();
		print(self.embeddings_index);
		exit();


		embeddings = [];
		for text in texts:
			for word in text.split(" "):
				word_embedding = compute_embeddings(word);
				embeddings.append(word_embedding);
			break;

	# compute embedding from word using the glove
	def compute_word_embedding(self, word):
		try:
			return self.embeddings_index[word];
		except:
			return None;


 
	def compute_embedding_dictionary(self):
		# Load the whole embedding matrix
		embeddings_index = {}
		with open('./glove/glove.twitter.27B.25d.txt', encoding='utf-8') as f:
			for line in f:
				values = line.split()
				word = values[0]
				embed = np.array(values[1:], dtype=np.float32)
				embeddings_index[word] = embed
		self.embeddings_index = embeddings_index;
		return

	# --------------- Potentially scrap this ---------
	def prepare_text_data(self, csv_file, VALIDATION_SPLIT=0.2):
		df = pd.read_csv(csv_file, delimiter=',');

		# For computation save
		df = df.tail(n=10);
		#print(df);

		# --- Prepare the texts ----
		texts = df['post'].tolist();

		#print(texts);

		# Text tokenization
		tokenizer = Tokenizer(num_words=self.MAX_NB_WORDS);
		tokenizer.fit_on_texts(str(texts));
		sequences = tokenizer.texts_to_sequences(texts);

		self.word_index = tokenizer.word_index;
		print('[!] Found %s unique tokens.' % len(self.word_index));

		data = pad_sequences(sequences, maxlen=self.MAX_SEQUENCE_LENGTH);

		
		# --- create one hot encoding for outputs ---
		personality_df = df['type'];
		

		labels = np.array(self.one_hot_encode(personality_df));

		#print(personality_df);
		#print(output_arr.shape);
		#print(self.get_personality_from_encoding(output_arr));

		print('[+] Shape of data tensor: {}'.format(data.shape));
		print('[+] Shape of label tensor: {}'.format(labels.shape))

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


		# Debug
		# print(x_train.shape);
		# print(y_train.shape);
		# print(x_train);
		# print(y_train);


		return (x_train,y_train,x_val,y_val);

	def get_embedding_layer(self):
		embedding_matrix = self.get_embedding_matrix(self.word_index);
		print(embedding_matrix);

		embedding_layer = Embedding(len(word_index) + 1,
								self.EMBEDDING_DIM,
								weights=[embedding_matrix],
								input_length=self.MAX_SEQUENCE_LENGTH,
								trainable=False);

		return embedding_layer;

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

	def get_embedding_matrix(self, word_index):
		# Prepare embedding layer
		embeddings_index = {}
		print(os.path.join(self.GLOVE_DIR, 'glove.twitter.27B.100d.txt'));
		f = open(os.path.join(self.GLOVE_DIR, 'glove.twitter.27B.100d.txt'))
		for line in f:
			values = line.split()
			word = values[0]
			coefs = np.asarray(values[1:], dtype='float32')
			embeddings_index[word] = coefs
		f.close()

		print('[!] Found %s word vectors.' % len(embeddings_index))

		embedding_matrix = np.zeros((len(word_index) + 1, self.EMBEDDING_DIM))
		for word, i in word_index.items():
			embedding_vector = embeddings_index.get(word)
			if embedding_vector is not None:
				# words not found in embedding index will be all-zeros.
				embedding_matrix[i] = embedding_vector

		return embedding_matrix;



if __name__ == "__main__":
	glove_dir = "./glove";
	wb = WordEmbedder(glove_dir);

	# Run 1
	#preprocessed_data = "./Dataset/clean_mbti.csv";
	#(x_train,y_train,x_val,y_val) = wb.prepare_text_data(preprocessed_data);
	#embedding_layer = wb.get_embedding_layer();

	# Run 2
	preprocessed_data = "./Dataset/clean_mbti.csv";
	wb.prepare_text_data_2(preprocessed_data);


