# --- libs ---
from WordEmb2 import WordEmbedder
from data_parser import DataParser
import sklearn

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import numpy as np
 
# --- Good ol main ---
def main():
	# word embeddings
	wb = WordEmbedder(embedding_index='./embeddings_index.pickle');
	#wb = WordEmbedder();

	# load the data (one big post data)
	preprocessed_data = "./Dataset/clean_mbti_v2.csv";

	# get train and test
	(X_train, Y_train, X_test, Y_test) = wb.prepare_text_data(preprocessed_data);

	print("[+] X_train shape: " + str(X_train.shape));
	print("[+] Y_train shape: " + str(Y_train.shape));
	print("[+] X_test shape: " + str(X_test.shape));
	print("[+] Y_test shape: " + str(Y_test.shape));





	# --- ML time :) ----
	model = XGBClassifier();
	model.fit(X_train, Y_train.ravel());

	# Loading classifier
	s = pickle.dump(model, open('xgboost_model.pickle', 'wb'));
	classifier = pickle.load(open('xgboost_model.pickle','rb'));

	text_test = ["hello world"];
	embeddings_from_test = np.array(wb.compute_embeddings(["hello world"], wb.embedding_index));
	embedding_avgs = wb.compute_average(embeddings_from_test);
	print(len(embeddings_from_test));

	print(wb.compute_average(embeddings_from_test).shape);
	print(classifier.predict(embedding_avgs));
	

	return;


if __name__ == "__main__":
	main();