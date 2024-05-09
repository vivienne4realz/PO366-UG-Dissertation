import praw
import datetime 
import pandas as pd
import time 
import re 

user_agent = "Reddit_Scrapper 1.0 by /u//FeatureChoice5036"
reddit = praw.Reddit(
 client_id="MTd8ExEw9RmlGUhMxebPKw",
 client_secret="XUClAjJfhT7SjcdrQzakRdKclTyGSA",
 user_agent=user_agent
)

# Hot new rising topics

filename_1 = "singaporeraw_elite.txt"
file = open(filename_1, 'w')

my_keywords = ['elite']

with open(filename_1, 'w') as file:
    for submission in reddit.subreddit("SingaporeRaw").top(limit=None): # need to give reason why this subreddit
        #stext = submission.selftext.lower()
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            cbody = comment.body.lower()
            time.sleep(0.1)
            if any(keyword in cbody for keyword in my_keywords):
                cbody = re.sub(r'\n+', ' ', cbody) # removes ALL new lines within the comments, replacing them with a single space
                file.write(comment.body + "\n") # each new comment to be in a new line



