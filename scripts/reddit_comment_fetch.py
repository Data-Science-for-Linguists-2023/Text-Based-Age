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
    comments.to_csv(f'{filename}_comments.csv')
    

def traverse_data(posts, filename): 
    count = 0
    all_comments = []
    for post in posts:
        submission = reddit.submission(id=post.id)
        submission.comments.replace_more(limit=None)
        comments = submission.comments.list()
        sorted_comments = sorted(comments, key=lambda comment: comment.score, reverse=True)
        for comment in sorted_comments[2:32]:
            all_comments.append(comment.body)
            if count % 100 == 0:
                save_comments(all_comments, filename)
                print('another 100')
            count += 1



if __name__ == '__main__':
    sub = 'askteenboys'
    subreddit = reddit.subreddit(sub)
    posts = subreddit.top(limit=100)
    traverse_data(posts, sub)