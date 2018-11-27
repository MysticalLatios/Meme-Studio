#File for facilitating sharing

#Twitter
import tweepy

#Secrets
consumer_key ="xxxxxxxxxxxxxxxx"
consumer_secret ="xxxxxxxxxxxxxxxx"
access_token ="xxxxxxxxxxxxxxxx"
access_token_secret ="xxxxxxxxxxxxxxxx"


def tweet(path_to_image, text_of__tweet):
    #Auth
    AUTH = tweepy.OAuthHandler(consumer_key, consumer_secret)
    AUTH.set_access_token(access_token, access_token_secret)

    API = tweepy.API(AUTH)
    tweet = text_of__tweet
    image_path = path_to_image

    # to attach the media file
    status = API.update_with_media(image_path, tweet)
    API.update_status(status = tweet)