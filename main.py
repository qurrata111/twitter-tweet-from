import tweepy

# personal information
consumer_key = ' '
consumer_secret = ' '
access_token = ' '
access_token_secret = ' '

# set up OAuth dan integrasi dengan API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# tweet somethin'
tweet = input('What\'s on your thought? ')
wantToUploadImg = input('Want to upload image? Yes/No ')
if (wantToUploadImg.lower() == "yes"):
	image_path = input("drop the path of image ")
	status = api.update_with_media(image_path, tweet)
api.update_status(status=tweet)