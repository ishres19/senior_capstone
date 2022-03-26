import json
import pandas as pd
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# from textblob import TextBlob

# file_content = open('2020-12-randomlychosen.jsonl', "r")

def convert_json_to_dataframe(filename, year_month):
	
	df = pd.read_json(filename, lines = True)
	df = df[df['lang'].str.contains('en|uk', regex=True)]
	df = df[['created_at','id','full_text','geo','coordinates','place', 'lang', 'retweeted_status']]
	df.to_csv('monthly_tweets_dataframe/'+year_month+'.csv', index=False)	

convert_json_to_dataframe('/eccs/home/ishres19/COVID-19-TweetIDs/2020-2021/2020-11-randomlychosen.jsonl', '2020_11')




