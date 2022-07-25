def create_youtube_video(title, desc, hash=[]): # creates a dict with a title, description, likes and dislikes counter and comments
	hash = hash[:5:]
	return {'title':title, "description":desc, 'likes':0, 'dislikes':0, 'comments':{}, 'hashtag':hash} #creates and returns the dict on the same row to save space a bit + I am lazy



def like(vid): # raises the video amount of likes
	if 'likes' in vid: # checks if it is a video dict from create_youtube_video()
		vid['likes'] += 1 # adds one to likes
	return vid


def dislike(vid): # raises the video amount of dislikes
	if 'dislikes' in vid: # checks if it is a video dict from create_youtube_video()
		vid['dislikes'] += 1 # adds one to the dislikes
	return vid


def add_comment(vid, username, content): # adds a comment to the comments dict inside of the video dict
	if 'comments' in vid: # checks if it is a video dict from create_youtube_video()
		vid['comments'][username] = content # adds the comment
	return vid


def similarity_to_video(vid1, vid2): # trakes two videos and checks their hashtag's similarity precantage (100 % means that they are the same or that one is contained inside of the other)
	if 'hashtag' in vid1 and 'hashtag' in vid2: # checks if both dicts are video dicts from create_youtube_video()
		hash1 = vid1['hashtag'] # defines a list of the hashtags for the first video
		hash2 = vid2['hashtag'] # defines a list of the hashtags for the second video
		score = 0 # sets score
		if len(hash1) > len(hash2): # checks if the second video has a smaller hashtag list than the first
			for tag in hash2: # if it is shorter does the deafult but with hash1 and hash2 switched
				if tag in hash1:
					score += 1
			return f'{score/len(hash2)*100} %' # returns it in a nice presantage value

		for tag in hash1: # if they are the same length or the first is shorter it does it with the first
			if tag in hash2: # checks for each tag if its in the other hash list and if it is it adds one
				score += 1
		return f'{score/len(hash1)*100} %' # returns it in a nice presantage value