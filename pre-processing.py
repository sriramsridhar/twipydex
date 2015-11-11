import csv
import re

def processTweet(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    #remove \x
    tweet= re.sub(r'(\\x[^\s]+)','',tweet)
    #remove []
    tweet=re.sub(r'\[','',tweet)
    tweet=re.sub(r'\]','',tweet)
    #remove , '
    tweet=re.sub(r'\,','',tweet)
    tweet=re.sub(r'\'','',tweet)
    # remove rt
    tweet=re.sub(r'rt','',tweet)
    return tweet

fp=open('kabali-pp.txt','w')
with open('kabali.csv','rU') as cf:
    reader=csv.reader(cf,delimiter=' ')
    for row in reader:
        tweet=str(row)
        pTweet=processTweet(tweet)
        fp.write(pTweet+"\n")
fp.close()


                 

