import pandas as pd
import os  

def append_files():
	path_of_directory = '/Users/irisa/senior_capstone_sentiment_analysis/monthly_tweets_dataframe/Textblob_analysis/'
	df1 = pd.DataFrame()
	for csv_file in os.listdir(path_of_directory):
		if csv_file.endswith('.csv'):
			file1 = pd.read_csv(csv_file) 
			if df1.empty:
				df1 = file1
			df1 = pd.concat([df1, file1])
	df1.to_csv('final.csv')
			
append_files()