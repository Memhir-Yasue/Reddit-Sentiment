from textblob import TextBlob
import praw
import config

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     user_agent="Sentiment on reddit V 0.001")


def version001(): #Prints sentiment of each post
	for submission in reddit.subreddit('Temple').hot(limit=50):
		title = TextBlob(submission.title)
		score = title.sentiment.polarity
		if (score != 0):
		    print(title, score) # Encoding to avoid error on cmd
# version01()

def version005(): # Prints sentiment of each comment per post
	for submission in reddit.subreddit('Temple').hot(limit=20):
		title = submission.title
		comments = submission.comments
		for comment in comments:
			string_comment = TextBlob(comment.body)
			score = string_comment.sentiment.polarity
			if (score != 0):
				print(title,': ',string_comment,': ', score)
				print('\n')
# version015()

def version100(): # Print the average sentiment of the comments per post
	i = 1
	for submission in reddit.subreddit('depression').hot(limit=20):
		title = submission.title
		comments = submission.comments
		score_Array = [] 							# Score from each comment
		comments.replace_more(limit=0) 				# To stop the 'MoreComments object has no attribute body' error
		for comment in comments:
			string_comment = TextBlob(comment.body)
			score = string_comment.sentiment.polarity
			score_Array.append(score)
		nc = len(score_Array)						# nc = # of comment
		if (nc!=0): 								# To avoid posts with no comments on them
			avrg_Score = sum(score_Array)/nc 		# Average polarity for all comments.
			print(i,': ',title,':  ',avrg_Score)
			print('\n')
		i+=1


# def version103(): # Include the post's mainbody in sentiment calculation

def version105(): # Print the average sentiment for a subreddit
	i = 1
	subreddit_score = []
	for submission in reddit.subreddit('UPenn').hot(limit=900):
		title = submission.title
		comments = submission.comments
		score_Array = [] 							# Score from each comment
		comments.replace_more(limit=0) 				# To stop the 'MoreComments object has no attribute body' error
		for comment in comments:
			string_comment = TextBlob(comment.body)
			score = string_comment.sentiment.polarity
			score_Array.append(score)
		nc = len(score_Array)						# nc = # of comment
		if (nc!=0): 								# To avoid posts with no comments on them
			avrg_Score = sum(score_Array)/nc 		# Average polarity for all comments.
			subreddit_score.append(avrg_Score)
		print(i)
		i+=1
	avrg_subscore = float(sum(subreddit_score))/float(len(subreddit_score))
	print(avrg_subscore)



from matplotlib import pyplot as plt
def version106(): #Modified V.01 with matplot for graphing
	score_list = []
	index_list = []
	for submission in reddit.subreddit('depression').hot(limit=900):
		title = TextBlob(submission.title)
		score = title.sentiment.polarity
		score_list.append(score)
	for i in range(len(score_list)):
		index_list.append(i)
	plt.plot(index_list,score_list)
	plt.show()

def version107():
	score_list = [TextBlob(submission.title).sentiment.polarity 
	for submission in reddit.subreddit('Temple').hot(limit=500) ]
	print(score_list)

def version108():
	i = 1
	subreddit_score = []
	avrgscore_list = []
	index_list = []
	for submission in reddit.subreddit('depression').hot(limit=900):
		title = submission.title
		comments = submission.comments
		score_Array = [] 							# Score from each comment
		comments.replace_more(limit=0) 				# To stop the 'MoreComments object has no attribute body' error
		for comment in comments:
			string_comment = TextBlob(comment.body)
			score = string_comment.sentiment.polarity
			score_Array.append(score)
		nc = len(score_Array)						# nc = # of comment
		if (nc!=0): 								# To avoid posts with no comments on them
			avrg_Score = sum(score_Array)/nc 		# Average polarity for all comments.
			subreddit_score.append(avrg_Score)
		print(i)
		i+=1
		avrg_subscore = float(sum(subreddit_score))/float(len(subreddit_score))
		avrgscore_list.append(avrg_subscore)
	for j in range(len(avrgscore_list)):
		index_list.append(j)
	plt.plot(index_list, avrgscore_list)
	plt.show()
version108()	