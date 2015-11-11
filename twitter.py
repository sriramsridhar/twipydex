import tweepy
import json
import csv
import time


consumer_key = "MNIWwfj1BMpL5XrDYb4YotrFK"
consumer_secret = "ZSK0fCeT78TG6zptHbR8JrsnOAB8BKWGBB0q8jx1ldYzYfCYnm"

access_token = "132813210-Wu6aCnnxOPvbotu2kCXu33W1I2DMHVRrFN0Y4zPV"
access_token_secret = "FOqGMGPs5DXJkWkFqTZavSZ1Li5vD7jusQsp7gcV0PIKR"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth)

csvFile=open('kabali.csv','w')
csvWriter=csv.writer(csvFile)

c = tweepy.Cursor(api.search, q="Kabali",lang="en").items(1000)
while True: 
        try:
                tweet=c.next()
                print "Text :" + tweet.text + " Created at : " + str(tweet.created_at) + "\n"
                csvWriter.writerow([tweet.text.encode('utf-8')])
        except tweepy.TweepError:           
                time.sleep(2)
                continue
        except StopIteration:
                break    
csvFile.close()



            
	

