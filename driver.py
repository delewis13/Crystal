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

import preprocessor as p

# --- Global variables ---
personality_types = ['INFJ', 'ENTP', 'INTP', 'INTJ', 'ENTJ', 'ENFJ', 'INFP', 'ENFP', 
					'ISFP', 'ISTP', 'ISFJ', 'ISTJ', 'ESTP', 'ESFP', 'ESTJ', 'ESFJ'];
# --- Classifier func ---
def get_metrics(model, X_test, Y_test):
	# Get predictions
	y_pred = model.predict(X_test);

	# Accuracy
	print('[+] Accuracy');
	print(accuracy_score(Y_test, y_pred));
	print("\n\n");

	# evaluate predictions
	print('[+] Classification report');
	print(classification_report(Y_test, y_pred));

def predict_personality_from_post(model, post, wb):
	# Preprocess the tweets
	post = p.tokenize(post);
	#print(post);

	# Grab the embeddings and averages
	embeddings_from_post = np.array(wb.compute_embeddings([post], wb.embedding_index));
	embedding_avgs = wb.compute_average(embeddings_from_post);

	print('[+] Embedding length from test text: ' + str(len(embeddings_from_post)));
	print(wb.compute_average(embeddings_from_post).shape);
	print('[+] Prediction: ');

	# Compute the prediction
	prediction = model.predict(embedding_avgs);
	print(prediction);

	# Get personality type 
	index_personality = prediction[0] - 1;
	personality_type = personality_types[index_personality];

	return personality_type;

 
# --- Good ol main ---
def main():
	# word embeddings
	wb = WordEmbedder(embedding_index='./embeddings_index.pickle');
	#wb = WordEmbedder();

	# load the data (one big post data)
	preprocessed_data = "./Dataset/clean_mbti_v2.csv";

	# get train and test
	#(X_train, Y_train, X_test, Y_test) = wb.prepare_text_data(preprocessed_data);
	data_pkl = './data.pickle';
	labels_pkl = './labels.pickle';
	(X_train, Y_train, X_test, Y_test) = wb.prep_data_from_pickle(data_pkl, labels_pkl, 
													VALIDATION_SPLIT=0.2);

	print("[+] X_train shape: " + str(X_train.shape));
	print("[+] Y_train shape: " + str(Y_train.shape));
	print("[+] X_test shape: " + str(X_test.shape));
	print("[+] Y_test shape: " + str(Y_test.shape));

	Y_train = np.argmax(Y_train, axis=1);
	Y_test = np.argmax(Y_test, axis=1);

	# --- ML time :) ----
	print('[+] Training model...')
	model = XGBClassifier();
	model.fit(X_train, Y_train.ravel());
	model.fit(X_train, Y_train);
	print('[+] Model trained!');

	# Loading classifier
	print('[+] Picklizing model!');
	print();
	s = pickle.dump(model, open('xgboost_model.pickle', 'wb'));

	# ---- Loading the classifier ---
	print('[+] Loading model!');
	classifier = pickle.load(open('xgboost_model.pickle','rb'));
	print();

	# --- Classifier metrics evaluation ---
	# Evaluate the metrics
	print('[+] Evaluating the metrics')
	get_metrics(classifier, X_test, Y_test);


	# --- Testing classifier ----
	# Predicted personality type given post
	print("\n\n");
	post = "hello world. I love to personal growth!";
	post = "... when you don't start to think about how you will spend your Sunday before Saturday evening. ... when you are easily able to order a meal without even having seen the menu. ... when you choose... Sorry, gotta make a post here once more ... stupid dilemma. Grr. :rolleyes: Anyways: Uhm, no, I don't think so ^^. ENTP is ENTP, ENTJ is ENTJ as far as I can tell $SMILEY$. I confess that I had mistyped myself. :th_woot: :th_woot: :th_woot: :th_woot: :th_woot: I have spent quite some time with the ENTJ's, actually I did like it. I just said farewell to them,... Hey guys, I just did some Socionics research (didn't e$SMILEY$e myself to socionics at all, up until now) and this really opened my eyes. I've always analysed only my behaviour, which is pretty... Psyduck (in German: Enton) I like his attitude. I think the truth about him is that he is an omniscient being and loves sarcasm. Think of this if you watch him. He tends to ridicule everyone ^^.... You're welcome $SMILEY$. Well, it unnerves the one stared on aswell as the one that stares. It is awkward and creepy if you stare at someone in a conversation as it is if you don't look at your... What walking tourist wrote came also up to my mind right away. But even before analyzing your current interests I would want to ask you if that tiny world of yours generally disturbs you. Does it?... Hey there, I think you described that reason for you being shy very well. In one word: Fear. You fear that people could possibly not like you if you would let go and relax, if you would not... ENTJ-professional-tip: Look on their nose bridges. At first this will maybe feel a little bit awkward, but if you do that it is actually easier than looking them into their eyes AND it is more... As you wish. You make sense, so I shall respect your needs. I'm going to get in touch with you before the mentioned zombie purge will be initiated. Gotta stash some more cigs and drinks then. Jup. But it won't come that far. I'll end the apocalypse before abstinence syndroms even will occur. I have lots of beer. And lots of cigarettes. Therefore I am prepared. Imagine a Zombie Apocalypse without beer and cigarettes ... nope. Won't happen to me. Got no weapons but I do know great... beep-beep-beep-beep-beep *rose-colored-glasses-alert-goes-off* It's good that you started this thread. Because now we maybe can do a good deed and can save your tender heart from getting blown... I can do it in two words - but to make my post legit I'll add a third, random one: bright - dark - batrachomyomachy Hello from Baden-W√ºrttemberg ^^. Having signed in to be an active part of the community will certainly help you on your journey to find yourself. Actually I don't think that you're only... Right. Make posts, not love! :laughing: <NUMBER> A variety of Murphy's Law: What can happen will happen. So your combination is no surprise, as it has to exist. By the way: Doesn't every EXXX $NUMBER$wX appear to be unusual at a first glance?... Never mind, just wanted to comment that one ^^. Here do you find the Enneagram-Area. Then pick a type, for Example Type <NUMBER> Forum and then look for Timeless' Descriptions. They're there for every... Hey there smnparish, you won't be able to answer all of your questions with MBTI only. I think both, INTJ and INTP could be your possible types. What Krusmynt wrote makes sense, but just... Hello there, it's always good to have people with cat avatars around. We can never have enough of you guys. Yours is especially awesome. Van Gogh Grumpy Cat Power so stronk! Regards, Ludwig You shall be forgiven! :laughing: I didn't think you were being serious there, J/k has been spotted! :ninja: But if NT's would only breed NT's you would be right ^^. You might be an ENTJ if you sigh when people around you say OMG, I don't know what to do first, this is too much, I'll fail and tell them: Obviously: going a), b), c), d), e) will be the right... Such wisdom. Much wow :blushed:. After reading some of your posts, I ascertain beyond doubt that you are both: scholar and oracle! It's a lie! But I have to admit that your assumption,... carolineatlantis If you really like him (as you say) and he does like you (even if he appears to just like you a little bit), I have one advice for you: Forget about MBTI and talk to him.... Started League of Legends again. Got demoted to Gold IV ... awww. Sad when being inactive gets punished in a game. Nevertheless amazing and fun to play ^^. Server: EUW Nickname: All is One ... Fair enough. Cheers. implement$SMILEY$und_of_glass_and_porcelain_touching Here you go: <NUMBER> It says good morning as it is $NUMBER$:57 am here and I just got up ^^. Join us. It's fun! Here, *handsheracupofcoffee* this one is on me. :wink: Once I've been to Australia. Wanted to drink a cup of coffee, went to some fancy coffee shop. Ordered a cup of coffee, please. Barista was kind of dissatisfied with my obviously sheepish order -... Really? This is interesting, never thought about that. Could you elaborate on what is especially Very German about her? I'm curious <SMILEY> Trolling mostly is exhausting to watch as it tends to be pretty primitive. But I have to admit that there are cases that, despite them being primitive, still make me laugh out very loud $SMILEY$. This... Well, what you say is absolutely true. If you see that a person would be better without you and you care for that person, you let go. Very noble. I did that once, but still I felt pretty bad... $HASHTAG$. Sorry :rolleyes:. Definitely Falkor the Luckdragon from The Neverending Story. Awwwwww. Much love Falkor <3. <NUMBER> If the belong interferes, we could easily replace it with is with you. So if the pen is only with you because you're holding it, you obviously didn't let go. Which is wrong imo. But you don't... Well, I'm ENTJ. Maybe because of that I can't comprehend that one could possibly secretly want something but not go for it. If one really wants it, that is. So if you really want it, ($MENTION$... You can compare anything with everything to e$SMILEY$lain something else. Sometimes it limps a bit but mostly it works fine ^^. I'm pretty aware that a human beeing can not equally be compared with a pen.... I'm not Christian, but I can still give you my philosophical answer ^^: Imagine you are holding a pen in your hand, standing in a public area where lots of people are. The pen belongs to you... Final Fantasy XIII - There was a special offer on Steam this weekend. HAD to buy it, only ‚Ç¨ <NUMBER> *yey* $SMILEY$. Welcome to PerC, enjoy the ride $SMILEY$. Yesterday a friend of mine presented me a bottle of Jack Daniels Single Barrel <NUMBER> as a dedication gift for my house. Well ... to be honest: Both of us didn't really enjoy drinking it ...... O.k. I'm done, I can't read this thread anymore, this is too much ... bye guys *runs out* :laughing: :laughing: :laughing: Gatts from Berserk! (OldSchool ^^) <NUMBER> Edward Elric from Full Metal Alchemist <NUMBER> Kirito from Sword Art Online In my opinion most people can understand this concept. It is not that complicated or abstract, therefore understanding it shouldn't be the problem. So it's not that nearly no one understands, it's... Haha, I did not see any of these because I never had and don't have a TV :laughing:. And jup, I DO live under a rock ^^. I think that this is where it all comes from $SMILEY$roud:. Just a few days ago when I was sitting in a little caf√© in downtown, a friend of mine and me were talking about exactly the same topic. At some point in this conversation I remembered something I... Lawl, I thought of it being an - to me yet unknown - idiom, so I actually didn't get two things there (the not obvious second has been hidden behind the, also not obvious, but... Hm, may I ask what this means? I'm not a native speaker, maybe therefore I didn't get it oO. Ok, I didn't get that one, either $SMILEY$. Plz e$SMILEY$lain :confused: I think I speak in everyones name if I say: You're welcome $SMILEY$roud:. Instead of just trying to memorize our writings, I suggest that you copy & paste this thread into a word-document on your..."
	post = "I like apples and long walks on the beach. How about you? I LOVE everyone and everything in existence";
	#print('[+] Post: ' + str(post)); 
	personality_type = predict_personality_from_post(classifier, post, wb);

	print('[+] Predicted personality type: ');
	print(personality_type);

	

	return;


if __name__ == "__main__":
	main();