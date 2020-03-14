import praw
import os

if __name__ == '__main__':
    
    client_id = os.getenv('CLIENT_ID', 'Token not gound...')
    client_secret = os.getenv('CLIENT_SECRET', 'Token not found...')
    password = os.getenv('PASSWORD', 'Token not found...')
    user_agent = os.getenv('USER_AGENT', 'Token not found...')
    username = os.getenv('USERNAME', 'Token not found...')

    reddit = praw.Reddit(client_id=client_id,
                    client_secret=client_secret,
                    password=password,
                    user_agent=user_agent,
                    username=username)
    
    print(reddit.user.me())

    # TODO assign as command argument
    subreddit_arg = "movies"  
    query_sub = reddit.subreddit(subreddit_arg)

    for idx, submission in enumerate(query_sub.hot(limit=25)):
        print(str(idx) + ". " + submission.title + "\n")

    # subreddit_name = 'cars'
    # red = praw.Reddit('User Auth') # figure out legitimate user authentication string
    # the_subreddit = red.get_subreddit(subreddit_name)

    # # get_top_submissions(red, subreddit_name='cars', ret_num=25)
    
    # #test_submission = get_top_submissions(red, 'cars', ret_num = 1)[0]
    # #get_comments_from_submission(test_submission)

    print('All done!')