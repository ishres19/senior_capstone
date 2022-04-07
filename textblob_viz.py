import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import plotly.express as px


def viz(file_name):
	df = pd.read_csv(file_name)
	print (df)	
	fig = px.line(df, x='created_at', y='mean')	
	fig.update_xaxes(nticks=30)
	fig.write_html("plot.html")

viz('/Users/irisa/senior_capstone_sentiment_analysis/monthly_tweets_dataframe/VADER_analysis/compound_mean_2020_08.csv')
