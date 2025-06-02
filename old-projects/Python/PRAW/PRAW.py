import praw

#Create app on reddit to achieve the following information client_id & client_secret
reddit = praw.Reddit(client_id='[client_id]',
                     client_secret='[client_secret]',
                     username='[username]',
                     password='[password]',
                     user_agent='my user agent')

submission = reddit.submission(id='a7zss0')

for submission in reddit.subreddit('Python').hot(limit=10):
    print(submission)

