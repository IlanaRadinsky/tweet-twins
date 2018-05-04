make all: usersToHashtags.txt hashtagsToUsers.txt

usersToHashtags.txt hashtagsToUsers.txt: get_tweets.py
	python3 get_tweets.py 1000


