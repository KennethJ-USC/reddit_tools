import praw

def get_top_submissions(auth, subreddit_name='all', time='day', min_submission_score=-1, ret_num = 25):
    
    the_subreddit = auth.get_subreddit(subreddit_name)
    
    the_submissions = []

    if time == 'week':
        for submission in the_subreddit.get_top_from_week(limit=None):
            if submission.score >= min_submission_score & ret_num > 0:
                the_submissions.append(submission)
                ret_num -= 1
            else:
                break
    elif time == 'day':
        for submission in the_subreddit.get_top_from_day(limit=None):
            if submission.score >= min_submission_score & ret_num > 0:
                the_submissions.append(submission)
                ret_num -= 1
            else:
                break
    return the_submissions
    
def get_comments_from_submission(the_submission, min_comment_score=-1):
    the_comments = []

    print(type(the_submission))
    for comment in praw.helpers.flatten_tree(the_submission.comments):
        if isinstance(comment, praw.objects.Comment) and comment.score >= min_comment_score:
            print(comment.body)
            the_comments.append(comment)
    return the_comments



if __name__ == '__main__':
    

    subreddit_name = 'cars'
    red = praw.Reddit('User Auth') # figure out legitimate user authentication string
    the_subreddit = red.get_subreddit(subreddit_name)

    # get_top_submissions(red, subreddit_name='cars', ret_num=25)
    
    test_submission = get_top_submissions(red, 'cars', ret_num = 1)[0]
    get_comments_from_submission(test_submission)

    print('All done!')