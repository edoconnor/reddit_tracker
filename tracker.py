from psaw import PushshiftAPI
import pandas as pd
import datetime as dt

api = PushshiftAPI()

start_time = int(dt.datetime(2021, 4, 12).timestamp())

submissions = api.search_submissions(after=start_time,
                                     subreddit='wallstreetbets',
                                     filters=['url', 'author','title','subreddit'])

for submission in submissions:
    words = submission.title.split()
    cashtags = list(set(filter(lambda word: word.lower().startswith('$'), words)))

    if len(cashtags) > 0:
        print(cashtags)
        print(submission.created_utc)
        print(submission.title)