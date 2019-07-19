from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials


class TwitterStreamer():
 
  def stream_tweets(self, filename, hashtag) 
  
       listener = StdOutListener()
       auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
       auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

       stream = Stream(auth, listener)

       stream.filter(track=[hashtag])
  

class StdOutListener(StreamListener):
 
  def __init__(self, filename):
      self.filename = filename      

  def on_data(self, data):
      try:  
        print(data)
        with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
        return True
      except BaseException as e:
        print("Error on data %s" % str(e))
      return True
          
  def on_error(self, status):
      print(status)

if __name__ == "__main__":
  hash_tag_list = ["donald trump", "hillary clinton", "barack obama", "bernie sanders"]
  fetched_tweets_filename = "tweets.txt"

  twitter_streamer = TwitterStreamer()
  twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
      
