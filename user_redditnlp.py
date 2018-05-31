from textblob import TextBlob
import praw
import config

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     user_agent="Testing user smuggle")

def user_frm_subreddit():
	i = 0
	user = []
	for submission in reddit.subreddit('Temple').hot(limit=10):
		comments = submission.comments
		for comment in comments:
			i+=1
			user.append(comment.author)
			print(i, comment.author)
	return user

user = user_frm_subreddit()
print(user)

def comments_frm_user(user): # return an array with each element of the array being all the comments from each redditor
	print(len(user))
	all_comment = []
	for i in range(len(user)): # For all users 
		redditer = user[i]
		redditer_comment = []
		for comment in reddit.redditor(str(redditer)).comments.new(limit=50):	#Get 50 comments from each redditor
			# print(user[item],comment.body,'\n')
			redditer_comment.append(comment.body)
		all_comment.append(redditer_comment)			# store each collection of comments (from each redditor) into a list
		print(i,redditer, all_comment[i])
		print('\n')

	# for i in range(len(all_comment)):
	# 	print(i,all_comment[i],i)


comments_frm_user(user)