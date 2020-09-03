from celery import shared_task
from jpow_app.models import Ratio
import praw
from datetime import datetime
import pandas as pd
import numpy as np
import joblib
import re
import emoji

class cleanData(BaseEstimator, TransformerMixin):
    def processData(self, text):
        #replace emojis with text
        text = emoji.demojize(text, delimiters=("",""))
        #remove non-characters
        text = re.sub(r'([^a-zA-Z ]+?)', '', text)
        #remove single characters
        text =  re.sub(r"\b[a-zA-Z]\b", "", text)
        #multiple spaces into single spaces
        text = re.sub('\s+', ' ', text)
        #remove leading and trailing spaces
        text = re.sub(r"^\s+|\s+$", "", text)
        #convert to lowercase
        text = text.lower()
        #remove URLS
        text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
        #remove punctuation
        text = re.sub(r'[^\w\s]', '', text)
        return text

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = X.apply(self.processData)
        return X

#get comments current moves thread
def getComments():
    reddit = praw.Reddit(client_id = "CLIENT_ID",
                     client_secret = "CLIENT_SECRET",
                     user_agent = "USER_AGENT")
    subreddit = reddit.subreddit('wallstreetbets')
    comments = []
    for submission in subreddit.search("What Are Your Moves", time_filter = 'month', limit = 1):
        if "What Are Your Moves" not in submission.title:
            continue
        replies = submission.comments
        for top_level_comment in replies:
            if isinstance(top_level_comment, praw.models.MoreComments):
                continue
            comments.append(top_level_comment.body)
    return comments

#converts np array count to frequency dictionary
def frequencyArrayToDict(n):
    d = {}
    for i in range(0, len(n[0])):
        d[n[0][i]] = n[1][i]
    return d

#returns percetange of positive comments from predictions
def getPositiveSentiment(predictions):
    frequency_counts = np.unique(predictions, return_counts = True)
    d = frequencyArrayToDict(frequency_counts)
    posPct= 100* round(d['Bull']/(d['Bear'] + d['Bull']), 2)
    return int(posPct)

#create ratio object and adds to database
def updateRatio(posPct):
    today = datetime.now().strftime("%Y-%m-%d")
    p = Ratio(Date = today, PositiveSentiment = posPct)
    p.save()

@shared_task
def update():
    comments = getComments()
    toPredict = pd.Series(comments)
    model = joblib.load('classifier.pkl')
    predictions = model.predict(toPredict)
    posPct = getPositiveSentiment(predictions)
    updateRatio(posPct)
