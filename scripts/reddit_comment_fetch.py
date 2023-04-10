import praw
import pandas as pd
import time

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
        try:
            submission = reddit.submission(id=post.id)
            submission.comments.replace_more(limit=None)
            comments = submission.comments.list()
            sorted_comments = sorted(comments, key=lambda comment: comment.score, reverse=True)
            for comment in sorted_comments[2:32]:
                all_comments.append(comment.body)
                if count % 100 == 0:
                    save_comments(all_comments, filename)
                    print(f'Saved {len(all_comments)} comments for {filename}')
                count += 1
                time.sleep(1) # add a delay to avoid hitting Reddit's API rate limit
        except Exception as e:
            print(f'Error: {e}')
            continue

if __name__ == '__main__':
    subreddits = ['AskTeenGirls', 'AskTeenBoys', 'youngadults', 'college', 'LifeAfterSchool', 'AskWomenOver30', 'AskMenOver30']
    for sub in subreddits:
        subreddit = reddit.subreddit(sub)
        posts = subreddit.top(limit=100)
        traverse_data(posts, sub)