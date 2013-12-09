#from TwitterAPI import *
from unicodedata import normalize
#from NaiveBayes import *
from rawclassifier import *
import tweepy
class TwitterRequestHandler(object):
	def __init__(self, Tokens):
		self.OToken = Tokens[0]
		self.OSecret = Tokens[1]
		self.CKey = Tokens[2]
		self.CSecret = Tokens[3]
	def MakeRequest(self, GeoCode):

		contents = []
		classified_contents = {'sports' : [], 'finance' : [], 'personal' : []}
		if GeoCode == 'Invalid':
			return classified_contents
		auth = tweepy.OAuthHandler(self.CKey, self.CSecret)
		auth.set_access_token(self.OToken, self.OSecret)
		api = tweepy.API(auth)
		GeoCodeWithR = GeoCode + ',2mi'
		t = api.search(q = "", geocode = GeoCodeWithR, count = '20')
		TweetClassifier = RawClassifier()
		for tweet in t:
			result = TweetClassifier.FinalHandler(tweet.text)
			classified_contents[result].append(tweet.text)
			#contents.append(asc2_content)
		return classified_contents


if __name__ == "__main__":
	OAUTH_TOKEN = '913876524-iqDHk8QIq3AL6LRi34R4JGNGXekXG7yTubcp2lyK'
	OAUTH_SECRET = '8lXzL0JhwNsRktp51Ny6QN8kAtbckTXH0C0r9Uo0m0h1m'
	CONSUMER_KEY = '3NC3fjWZrRvTrppNrOrfIQ'
	CONSUMER_SECRET = 'XZRqEAUHWCjiNbd4Ve2Kk1WWVXvjDPqmq986DHP110'
	tokens = (OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
#	DB = DBBuilder()
	ReqHandler = TwitterRequestHandler(tokens);

	description = ReqHandler.MakeRequest()
	print description
