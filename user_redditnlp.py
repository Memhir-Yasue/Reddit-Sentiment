from textblob import TextBlob
import praw
import config
from operator import itemgetter # for sorting a specific index of an array. 
								# In this case, to sort by num of occurance while having the redditor name tied along side to it

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     user_agent="Testing user smuggle")

# ----------- old version ----------#
def user_frm_subreddit01(sub, z):
	user = []
	for submission in reddit.subreddit(sub).hot(limit=z):
		comments = submission.comments
		for comment in comments:
			user.append(comment.author)
	return user

def user_frm_subreddit(sub, z):
	main = []
	participation = [] # Number of occurence a redditor has commened on submissions
	user = []
	for submission in reddit.subreddit(sub).hot(limit=z):
		comments = submission.comments
		comments.replace_more(limit=0) 	
		for comment in comments:
			user.append(comment.author)
	for i in range (len(user)):
		num = user.count(user[i])
		participation.append(num)
		append_me = user[i], participation[i]
		main.append(append_me)
	main = list(set(main)) # remove duplicates 
	main_sorted =  sorted(main, key=itemgetter(1),reverse=True) # Sort by the first index of the array and reverse to make it largest to smallest
	return main_sorted

#
#	Part 1.5 (Already done??? not needed?)
#
def repetition(user):
	occurance_list = []
	name_list = []
	for i in range(len(user)):
		occurance = user.count(user[i])
		name = user[i]
		name_list.append(name)
		occurance_list.append(occurance)

# repetition(user)














#
#				FOR PART 2
#
def comments_frm_user(user): # return an array with each element of the array being all the comments from each redditor
	print(len(user))
	all_comment = []
	comments_frm_redditors = all_comment
	for i in range(len(user)): # For all users 
		redditer = user[i]
		redditer_comment = []
		for comment in reddit.redditor(str(redditer)).comments.new(limit=50):	#Get 50 comments from each redditor
			redditer_comment.append(comment.body)
		comments_frm_redditors.append(redditer_comment)			# store each collection of comments (from each redditor) into a list
		print(i,redditer, comments_frm_redditors)
		print('\n')

# comments_frm_user(user)