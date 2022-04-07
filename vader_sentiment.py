from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from pathlib import Path
import os
# df = pd.read_csv("2020_12.csv")

# csv_files = ['2020_01', '2020_02', '2020_03', '2020_04','2020_05', '2020_06', '2020_07',
# 			'2020_08', '2020_09', '2020_10', '2020_11', '2020_12']
path_of_directory = '/Users/irisa/senior_capstone_sentiment_analysis/monthly_tweets_dataframe'

def main():
	for csv_file in os.listdir(path_of_directory):
			if csv_file.endswith('.csv'):
				sentiment_analysis_of_tweets_vader(csv_file)

def sentiment_analysis_of_tweets_vader(id_file):
	print (id_file)
	analyzer = SentimentIntensityAnalyzer()
	df = pd.read_csv(id_file)
	df['compound'] = [analyzer.polarity_scores(x)['compound'] for x in df['full_text']]
	df['neg'] = [analyzer.polarity_scores(x)['neg'] for x in df['full_text']]
	df['neu'] = [analyzer.polarity_scores(x)['neu'] for x in df['full_text']]
	df['pos'] = [analyzer.polarity_scores(x)['pos'] for x in df['full_text']]
	
	df["created_at"] = df["created_at"].str.split().str[0]
	# df.to_csv('2020_12_sentiment.csv', index=False)	
	# df = pd.read_csv("2020_12_sentiment.csv")
	df['created_at'] = pd.to_datetime(df['created_at'])
	df['created_at'].dt.strftime('%m/%D/%Y')
	df['compound'] = df['compound'].astype(float)
	df_new = df[['created_at', 'compound']]
# 	print (df)
	# groupby_count_pos = df.groupby('created_at')['pos'].count()
# 	groupby_count_neg = df.groupby('created_at')['neg'].count()
# 	print (groupby_count_pos)
	group_by = df_new.groupby('created_at')['compound'].mean()
	print(group_by)
	groupby_df = group_by.to_frame(name = 'mean').reset_index()
	print (groupby_df)
	id_file = 'VADER_analysis/compound_mean' +'_' + id_file
	groupby_df.to_csv(id_file, index=False)


if __name__ == "__main__":
    main()

