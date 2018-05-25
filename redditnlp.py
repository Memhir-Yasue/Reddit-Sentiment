from textblob import TextBlob
from matplotlib import pyplot as plt
from flask import Flask, request, render_template, session
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
	for submission in reddit.subreddit('depression').hot(limit=20):
		title = submission.title
		comments = submission.comments
		for comment in comments:
			string_comment = TextBlob(comment.body)
			score = string_comment.sentiment.polarity
			if (score != 0):
				print(title,': ',string_comment,': ', score)
				print('\n')


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

def version103(): # Include the post's mainbody in average sentiment calculation
    i = 1
    for submission in reddit.subreddit('Temple').hot(limit=10):
    	i+=1
    	title = submission.title
    	comments = submission.comments
    	sub_body = TextBlob(submission.selftext)	# body text from the post's mainbody
    	sub_score = sub_body.sentiment.polarity
    	score_Array = []							# Score from each comment
    	score_Array.append(sub_score)
    	comments.replace_more(limit=0) 				# To stop the 'MoreComments object has no attribute body' error
    	# print(sub_body, sub_score)
    	# print('\n')
    	for comment in comments:
    		string_comment = TextBlob(comment.body)
    		score = string_comment.sentiment.polarity
    		score_Array.append(score)
    		nc = len(score_Array)						# nc = # of comment
    		if (nc!=0): 								# To avoid posts with no comments on them
    		    avrg_Score = sum(score_Array)/nc 		# Average polarity for all comments.
    		    print(i,': ',title,':  ',avrg_Score)
    		    print('\n')


def version105(): # Print the average sentiment for a subreddit
	i = 1
	subreddit_score = []
	for submission in reddit.subreddit('UPenn').hot(limit=900):
		title = submission.title
		comments = submission.comments
		sub_body = TextBlob(submission.selftext)
		sub_score = sub_body.sentiment.polarity
		score_Array = [] 							# Score from each comment
		score_Array.append(sub_score)
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

def version108(): # Displays the average sentiment as the number of submissions analyized increases
	i = 1
	subreddit_score = []
	avrgscore_list = []
	index_list = []
	for submission in reddit.subreddit('worldnews').hot(limit=50):
		title = submission.title
		comments = submission.comments
		sub_body = TextBlob(submission.selftext)
		sub_score = sub_body.sentiment.polarity
		score_Array = [] 							# Score from each comment
		score_Array.append(sub_score)
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


def version110(): # Display the average sentiment per post AND INCLUDE TITLE FOR SENTIMENT CALCULATION
	i = 1
	subreddit_score = []
	for submission in reddit.subreddit('depression').hot(limit=30):
		title = submission.title
		str_title = TextBlob(title)
		title_score = str_title.sentiment.polarity
		comments = submission.comments
		sub_body = TextBlob(submission.selftext)
		sub_score = sub_body.sentiment.polarity
		heading_score = title_score + sub_score
		score_Array = [] 							# Score from title, body and comment
		score_Array.append(title_score)
		score_Array.append(sub_score)
		comments.replace_more(limit=0) 				# To stop the 'MoreComments object has no attribute body' error
		for comment in comments:
			string_comment = TextBlob(comment.body)
			score = string_comment.sentiment.polarity
			score_Array.append(score)
		nc = len(score_Array)						# nc = # of comment
		avrg_Score = sum(score_Array)/(nc+1) 		# Average polarity for all comments.
		subreddit_score.append(avrg_Score)
		i+=1
		avrg_subscore = float(sum(subreddit_score))/float(len(subreddit_score))
		print(i,title, title_score, sub_score, avrg_subscore)

def test(): # testing for flask by calling this function via redditnlp.test() on flaskapp.py
	for i in range(10):
		return 'Hello World. This is coming from the test function'

def version111_flask():
	i = 1
	subreddit_score = []
	for submission in reddit.subreddit('depression').hot(limit=10):
		title = submission.title
		str_title = TextBlob(title)
		title_score = str_title.sentiment.polarity
		comments = submission.comments
		sub_body = TextBlob(submission.selftext)
		sub_score = sub_body.sentiment.polarity
		heading_score = title_score + sub_score
		score_Array = [] 							# Score from title, body and comment
		score_Array.append(title_score)
		score_Array.append(sub_score)
		comments.replace_more(limit=0) 				# To stop the 'MoreComments object has no attribute body' error
		for comment in comments:
			string_comment = TextBlob(comment.body)
			score = string_comment.sentiment.polarity
			score_Array.append(score)
		nc = len(score_Array)						# nc = # of comment
		avrg_Score = sum(score_Array)/(nc+1) 		# Average polarity for all comments.
		subreddit_score.append(avrg_Score)
		i+=1
		avrg_subscore = float(sum(subreddit_score))/float(len(subreddit_score))
		string_avrg_subscore = str(avrg_subscore)
		return (title,string_avrg_subscore)

def version120_flask(z):
	i = 1
	subreddit_score = []
	title_score_info = []
	for submission in reddit.subreddit('nevertellmetheodds').hot(limit=z):
		title = submission.title
		str_title = TextBlob(title)
		title_score = str_title.sentiment.polarity
		comments = submission.comments
		sub_body = TextBlob(submission.selftext)
		sub_score = sub_body.sentiment.polarity
		heading_score = title_score + sub_score
		score_Array = [] 							# Score from title, body and comment
		score_Array.append(title_score)
		score_Array.append(sub_score)
		comments.replace_more(limit=0) 				# To stop the 'MoreComments object has no attribute body' error
		for comment in comments:
			string_comment = TextBlob(comment.body)
			comment_score = string_comment.sentiment.polarity
			score_Array.append(comment_score)
		nc = len(score_Array)						# nc = # of comment
		avrg_Score = sum(score_Array)/(nc+1) 		# Average polarity for all comments.
		subreddit_score.append(avrg_Score)
		i+=1
		avrg_subscore = float(sum(subreddit_score))/float(len(subreddit_score))
		string_avrg_subscore = str(avrg_subscore)
		append_me = str(i),title,heading_score,comment_score
		# print(title_score_info)
		title_score_info.append(append_me)		
	return title_score_info
# 	print(title_score_info[0])
# version120_flask()
# def version200():
# 	import flaskclass
# 	flaskclass.index()

def version125_flask(sub, z): # Everything is now concatinated and one element
	i = 1
	subreddit_score = []
	title_score_info = []
	for submission in reddit.subreddit(sub).hot(limit=z):
		title = submission.title
		str_title = TextBlob(title)
		title_score = str_title.sentiment.polarity
		comments = submission.comments
		sub_body = TextBlob(submission.selftext)
		sub_score = sub_body.sentiment.polarity
		heading_score = title_score + sub_score
		score_Array = [] 							# Score from title, body and comment
		score_Array.append(title_score)
		score_Array.append(sub_score)
		comments.replace_more(limit=0) 				# To stop the 'MoreComments object has no attribute body' error
		for comment in comments:
			string_comment = TextBlob(comment.body)
			comment_score = string_comment.sentiment.polarity
			score_Array.append(comment_score)
		nc = len(score_Array)						# nc = # of comment
		avrg_Score = sum(score_Array)/(nc+1) 		# Average polarity for all comments.
		subreddit_score.append(avrg_Score)
		i+=1
		avrg_subscore = float(sum(subreddit_score))/float(len(subreddit_score))
		# string_avrg_subscore = str(avrg_subscore)
		append_me = str(i)+'. '+title+' ',(avrg_Score)
		# print(title_score_info)
		title_score_info.append(append_me)		
	return title_score_info # returns the concatinated title with sentiment score

def version125_dash(sub, z): # Return a list of sentiment for all comments per post
	i = 1
	subreddit_score = []
	title_score_info = []
	avrg_Score_list = [] # A list of avrg_score to return as a list for dash visualization
	for submission in reddit.subreddit(sub).hot(limit=z):
		title = submission.title
		str_title = TextBlob(title)
		title_score = str_title.sentiment.polarity
		comments = submission.comments
		sub_body = TextBlob(submission.selftext)
		sub_score = sub_body.sentiment.polarity
		heading_score = title_score + sub_score
		score_Array = [] 							# Score from title, body and comment
		score_Array.append(title_score)
		score_Array.append(sub_score)
		comments.replace_more(limit=0) 				# To stop the 'MoreComments object has no attribute body' error
		for comment in comments:
			string_comment = TextBlob(comment.body)
			comment_score = string_comment.sentiment.polarity
			score_Array.append(comment_score)
		nc = len(score_Array)						# nc = # of comment
		avrg_Score = sum(score_Array)/(nc+1) 		# Average polarity for all comments.
		subreddit_score.append(avrg_Score)
		i+=1
		avrg_subscore = float(sum(subreddit_score))/float(len(subreddit_score))
		# string_avrg_subscore = str(avrg_subscore)
		# append_me = str(i)+'. '+title+' '+str(heading_score)+' ',(avrg_Score)
		# print(title_score_info)
		# title_score_info.append(append_me)
		avrg_Score_list.append(avrg_Score)	
	return avrg_Score_list
# version125_dash()
###############################################################################
def version150_flask(sub, z): # Unweighted % of positive and negative sentiment
	i = 1
	avrg_Score_list = [] # A list of avrg_score to return as a list for dash visualization
	title_score_info = []
	for submission in reddit.subreddit(sub).hot(limit=z):
		pos_count = 1
		neg_count = 1
		pos_over_neg = 0							# % of positive comments
		neg_over_pos = 0							# % of negative comments		
		title = submission.title
		comments = submission.comments
		comments.replace_more(limit=0) 				# To stop the 'MoreComments object has no attribute body' error
		for comment in comments:					
			string_comment = TextBlob(comment.body)
			comment_score = string_comment.sentiment.polarity # comment sentiment (-1 to 1)
			if comment_score > 0:					# Count num of positive comments
				pos_count+=1
			if comment_score < 0:
				neg_count+=1						# Count num of negative comments
		pos_over_neg = (pos_count/(neg_count+pos_count))*100 # % of positive comments
		neg_over_pos = (neg_count/(pos_count+neg_count))*100 # % of negative comments	
		i+=1
		append_me = str(i)+'. '+title+' ',int(pos_over_neg),int(neg_over_pos)
		title_score_info.append(append_me)
		# print( str(i)+'. '+title+' ',pos_over_neg,neg_over_pos)
	return title_score_info	
# version150_flask('Temple',5)

def version160_flask(sub, z): # Unweighted % of positive and negative sentiment
	i = 1
	avrg_Score_list = [] # A list of avrg_score to return as a list for dash visualization
	title_score_info = []
	for submission in reddit.subreddit(sub).hot(limit=z):
		pos_count = 1
		neg_count = 1
		pos_over_neg = 0							# % of positive comments
		neg_over_pos = 0							# % of negative comments
		total_count = 0		
		title = submission.title
		comments = submission.comments
		comments.replace_more(limit=0) 				# To stop the 'MoreComments object has no attribute body' error
		for comment in comments:					
			string_comment = TextBlob(comment.body)
			comment_score = string_comment.sentiment.polarity # comment sentiment (-1 to 1)
			if comment_score > 0:					# Count num of positive comments
				pos_count+=1
			if comment_score < 0:
				neg_count+=1						# Count num of negative comments
		pos_over_neg = (pos_count/(neg_count+pos_count))*100 # % of positive comments
		neg_over_pos = (neg_count/(pos_count+neg_count))*100 # % of negative comments
		total_count = pos_count + neg_count	
		i+=1
		append_me = str(i)+'. '+title+' ',int(pos_over_neg),int(neg_over_pos), total_count
		title_score_info.append(append_me)
		# print( str(i)+'. '+title+' ',pos_over_neg,neg_over_pos)
	return title_score_info	

def version170_flask(sub,z): # Show score along side
	i = 1
	avrg_Score_list = [] # A list of avrg_score to return as a list for dash visualization
	title_score_info = []
	for submission in reddit.subreddit(sub).hot(limit=z):
		score_Array = [] # List of sentiment score
		average_score = 0
		pos_count = 1
		neg_count = 1
		pos_over_neg = 0							# % of positive comments
		neg_over_pos = 0							# % of negative comments
		total_count = 0		
		title = submission.title
		comments = submission.comments
		comments.replace_more(limit=0) 				# To stop the 'MoreComments object has no attribute body' error
		for comment in comments:					
			string_comment = TextBlob(comment.body)
			comment_score = string_comment.sentiment.polarity # comment sentiment (-1 to 1)
			score_Array.append(comment_score)
			if comment_score > 0:					# Count num of positive comments
				pos_count+=1
			if comment_score < 0:
				neg_count+=1						# Count num of negative comments
		pos_over_neg = (pos_count/(neg_count+pos_count))*100 # % of positive comments
		neg_over_pos = (neg_count/(pos_count+neg_count))*100 # % of negative comments
		total_count = pos_count + neg_count
		average_score = float(sum(score_Array))/float(len(score_Array)) # Average score 	
		i+=1
		append_me = str(i)+'. '+title+' ',int(pos_over_neg),int(neg_over_pos), total_count, average_score
		title_score_info.append(append_me)
		# print( str(i)+'. '+title+' ',pos_over_neg,neg_over_pos)
	return title_score_info	



# def main():
# 	version108()
# main()