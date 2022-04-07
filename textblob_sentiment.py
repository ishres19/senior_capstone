from textblob import TextBlob
import pandas as pd
import os
from pathlib import Path

path_of_directory = '/Users/irisa/senior_capstone_sentiment_analysis/monthly_tweets_dataframe'

def main():
	for csv_file in os.listdir(path_of_directory):
			if csv_file.endswith('.csv'):
				sentiment_analysis_of_tweets_textblob(csv_file)



def calculate_polarity(text):
	return TextBlob(text).sentiment.polarity

def calculate_subjectivity(text):
	return TextBlob(text).sentiment.subjectivity

def analysis_pos_neg(score):
	if score < 0:
		return 'Negative'
	if score ==0:
		return 'Neutral'
	else:
		return "Positive"

def sentiment_analysis_of_tweets_textblob(id_file):
	df = pd.read_csv(id_file)
	print (id_file)
	df['polarity'] = df['full_text'].apply(calculate_polarity)
	df['subjectivity'] = df['full_text'].apply(calculate_subjectivity)
	df['analysis'] = df['polarity'].apply(analysis_pos_neg)	
	df.to_csv('Textblob_analysis/sentiment_analysis' +'_'+id_file, index=False)	
	df["created_at"] = df["created_at"].str.split().str[0]
	# df.to_csv('2020_12_sentiment.csv', index=False)	
	# df = pd.read_csv("2020_12_sentiment.csv")
	df['created_at'] = pd.to_datetime(df['created_at'])
	df['created_at'].dt.strftime('%m/%D/%Y')
	df['polarity'] = df['polarity'].astype(float)
	df_new = df[['created_at', 'polarity']]

	group_by = df_new.groupby('created_at')['polarity'].mean()
	print(group_by)
	groupby_df = group_by.to_frame(name = 'mean').reset_index()
	print (groupby_df)
	id_file = 'Textblob_analysis/polarity_mean' +'_' + id_file
	lines = groupby_df.plot.line()
	groupby_df.to_csv(id_file, index=False)

if __name__ == "__main__":
    main()
