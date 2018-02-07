from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
consumer_key = "qwDf8s8UwrbPnSl70m8C6UQEo"
consumer_secret = "J9goLBGGMPty3CUfhw5iBFTJqqpV5QuIwzq3d091qiuBBa3PgU"
access_token = "803838215803248641-QUp4N73MIqKgoiTJgmXJqKOlKRP4tex"
access_token_secret = "aVZb6FrxQ4dQdp06cn7UKCTckcbxW0oWycUASafMrbJK3"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['>:(', ';(', ':*(']) 