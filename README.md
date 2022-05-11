# COVID-19 Sentiment Analysis

Nowadays, people use social media to express their feelings and thoughts regarding different topics. During the COVID-19 pandemic, people have been very active in social media, sharing information, personal experiences, and emotions. Twitter is one of the social media platforms where people are very active. Sentiment Analysis of Tweets can provide really interesting insights about the public’s preferences and sentiments. In this research, I will determine whether the sentiment changes of people’s COVID-19 related Tweets align with significant developments in the COVID-19 timeline.

![software architecture](https://user-images.githubusercontent.com/60153931/165425454-b628c360-ac8b-4d2e-bb02-b3733f13d082.jpg)

Software demonstration video: 
https://youtu.be/jc550G285kQ

How to Reproduce the results:

1. Clone the github directory with COVID-19 Tweet IDs -> https://github.com/echen102/COVID-19-TweetIDs
2. Create a Twitter Developer account
3. Clone this repository, and add the files to the directory with all the COVID-19 Tweet IDs
4. open the python file cleaning_up_files.py and edit the below lines, and run this file for all months: 
   Year = '2020-06'
   f = open("2020-2021/2020-06-randomlychosen.txt", "a+")
   (This code iterates over the all the Tweet-IDs in a file and take every 1000th Tweet ID, and adds it to a text file and to a '2020-2021')

6. open the python file 'hydrate.py' and change the line:
   data_dirs = ['2020-01', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12', 
            '2021-01', '2021-02', '2021-03', '2021-04', '2021-05', '2021-06', '2021-07', '2021-08', '2021-09', '2021-10', '2021-11', '2021-12', 
            '2022-01', '2022-02', '2022-03', '2022-04']
   to 
   data_dirs = ['2020-2021',]
8. run 'hydrate.py' to hydrate all the Tweet-IDs in the 2020-2021 directory
   - a bunch of json files will get created, one for each month
9. run the code json_file_to_pandas_dataframe.py for all json files for the year 2020
   - open this file and change the month and year from the below line, and change the path to wherever you cloned the above directory and repeat this        for all months:
     convert_json_to_dataframe('/eccs/home/ishres19/COVID-19-TweetIDs/2020-2021/2020-11-randomlychosen.jsonl', '2020_11')
   - This code creates a new directory monthly_tweets_dataframe and will store all the .csv files in it
6. You should have 12 .csv files for each month of 2020
8. VADER Sentiment: 
   1. add the file vader_sentiment.py to monthly_tweets_dataframe
   2. run vader_sentiment.py (creates a VADER_analysis directory with 12 .csv files, one for each month)
   3. add create_final_file.py to TextBlob_analysis directory
   4. run create_final_file.py (concats all the 12 .csv files into one
  
9.
   1. add the textblob_sentiment.py to monthly_tweets_dataframe
   2. run textblob_sentiment.py (creates a TextBlob_analysis directory with 12 .csv files, one for each month)
   3. add create_final_file.py to TextBlob_analysis directory
   4. run create_final_file.py (concats all the 12 .csv files into one)

