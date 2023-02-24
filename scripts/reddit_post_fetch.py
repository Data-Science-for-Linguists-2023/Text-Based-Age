import pickle
import praw
import pandas as pd

reddit = praw.Reddit(
    client_id='<YOUR CLIENT ID>',
    client_secret='<YOUR CLIENT SECRET>',
    user_agent='u/<USER ID> <VERSION> <BOT NAME>',
)

def save_comments(data, filename):
    comments = pd.DataFrame(data, columns=['comments'])
    comments.to_csv(f'{filename}._posts.csv')

def traverse_data(posts, filename): 
    count = 0
    all_data = []
    for post in posts:
        submission = reddit.submission(id=post.id)
        submission.comments.replace_more(limit=None)
        all_data.append(submission.selftext)
        print(submission.selftext)
        if count % 100 == 0:
            save_comments(all_data, filename)
            print('another 100')
        if count == 3000:
            return True
        count += 1

if __name__ == '__main__':
    sub = 'askteenboys'
    subreddit = reddit.subreddit(sub)
    posts = subreddit.top(limit=10000)
    traverse_data(posts, sub)