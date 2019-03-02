# Crystal

A Myers-Briggs personality predictor based on user social media posts [Facebook / Twitter supported].

See working demo at https://aiae.ml/crystal

# Predictions

Data is sourced from https://www.kaggle.com/datasnaek/mbti-type

Prediction pipeline:
- Initial cleaning via tweet-preprocessor [https://github.com/s/preprocessor]
- Word embeddings via GloVe trained on tweet data [https://nlp.stanford.edu/projects/glove/]
- Sentence embeddings via Bag-of-words
- XGBoost [similar to forest of random decision trees] for predictions

# Technologies

Backend:
- Flask

Frontend:
- React
- Redux

# Installation

Clone git repository.
Create a Python3 virtual environment via venv or Anaconda.
Install requirements [pip install -r requirements.txt].
Run Flask server within Flask_Server directory [python app.py]
