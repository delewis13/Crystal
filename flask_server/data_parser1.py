import pandas as pd
import preprocessor as p
import os



class DataParser():
	def __init__(self, csv_file):
		self.csv_file = csv_file
		self.row_list = []
		return

	def process_csv(self):
		# Convert the csv to a dataframe
		df = pd.read_csv(self.csv_file, delimiter=',')

		# Processed dataframes

		# For reference
		'''
		row_list = [];
		row_list.append({'type':'INFJ', 'posts':'hello'});
		row_list.append({'type':"INTP", 'posts':'hg'});
		print(row_list);
		print(pd.DataFrame(row_list));

		print(df['posts'].iloc[0])
		self.segment_posts(df['posts'].iloc[0]);

		'''

		personality_types = df['type'].unique().tolist()
		print(personality_types);
		for personality in personality_types:
			# print(personality);

			# print(df.loc[df['type'] == personality]);

			personality_df = df.loc[df['type'] == personality]
			for index, row in personality_df.iterrows():
				# One big post segment
				self.segment_posts_2(row['posts'], personality);

				# Single post segment
				#self.segment_posts(row['posts'], personality)
				# print(row['type'], self.segment_posts(row['posts'], personality));

		processed_df = pd.DataFrame(self.row_list)

		# DEBUG statements
		# print(self.row_list);
		# print(processed_df);

		# Save out DF to csv
		processed_df.to_csv(os.path.join('Dataset', 'clean_mbti_v2.csv'), index=False)

		return processed_df


	# segment posts into one whole string
	def segment_posts_2(self, posts, personality):
		post_split = posts.split("|||");
		final_post_list = [];
		for post in post_split:
			# Preprocess the tweets
			post = p.tokenize(post);
			post = self.post_process(post);

			# append to the final string
			final_post_list.append(post);

		final_post_str = " ".join(final_post_list);
		# Append to the row list
		one_personalit_one_big_post = {'type':personality, 'post':final_post_str};
		self.row_list.append(one_personalit_one_big_post);


	# segment posts and append to row_list
	def segment_posts(self, posts, personality):
		post_split = posts.split("|||");
		for post in post_split:
			# Preprocess the tweets
			post = p.tokenize(post);
			post = self.post_process(post);

			# append to row list
			one_personality_one_post = {'type':personality, 'post':post};
			self.row_list.append(one_personality_one_post);
		return;

	# post process the preprocess string
	def post_process(self, preprocessed_post):
		new_str = [];
		for word in preprocessed_post.split():
			if word.startswith('$') and word.endswith('$'):
				word = '<' + word[1:len(word)-1] + '>';
			new_str.append(word);
		new_str = " ".join(new_str);
		return new_str;

	def post_process_regex(self):
		
		return


	def create_datapoints(self):

		return

	# segment posts and append to row_list
	def segment_posts(self, posts, personality):
		post_split = posts.split("|||")
		for post in post_split:
			one_personality_one_post = {'type': personality, 'post': post};
			self.row_list.append(one_personality_one_post)
		return


if __name__ == "__main__":
	dataset = "./Dataset/mbti_1.csv"
	dp = DataParser(dataset)

	# One post
	# one_p_one_post_df = dp.process_csv();
	# print(one_p_one_post_df);
	# one_p_one_post_df = dp.process_csv()
	# print(one_p_one_post_df)

	# # Save the new processed df to csv
	# one_p_one_post_df.to_csv('./Dataset/clean_mbti.csv', index=False);

	# One big post one personality
	one_p_one_big_post_df = dp.process_csv();
	print(one_p_one_big_post_df);
	one_p_one_big_post_df.to_csv('./Dataset/clean_mbti_223.csv', index=False)

