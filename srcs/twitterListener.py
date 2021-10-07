# -*- coding: utf-8 -*-
'''
Python 3.7.3
[MSC v.1916 64 bit (AMD64)]
23 / 05 / 2021
@author: z_tjona
Cuando escribí este código, solo dios y yo sabíamos como funcionaba. Ahora solo lo sabe dios.
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''

from srcs.smser import sendSMS
from TwitterAPI import TwitterAPI
from os import getenv

from re import compile
from datetime import datetime
import pickle

'''Functions to handle and send emails
################################################### '''


import builtins
def print(*args, **kwargs):
    builtins.print(datetime.now(), '::: ', *args, **kwargs)


# ---- CONFIGS
pattern = compile('(#CastigoDivino.+@|.*@.+#CastigoDivino)')
twitterID = 125399079  # luisevivanco from https://commentpicker.com/twitter-id.php
numTweets = 10  # per call per period
period = 15  # minutes


# ----- VAR AUXS
try:
    with open("p.pickle", "rb") as f:
        lastTweet = pickle.load(f)
except:
    print('Pickle not found, default is generated.')
    lastTweet = ''  # id of the last analysed tweet

# ---- Connecting twitter
a = getenv("TWITTER_API_KEY")
b = getenv("TWITTER_API_SECRET")
c = getenv("TWITTER_ACCESS")
d = getenv("TWITTER_ACCESS_SECRET")

api = TwitterAPI(a, b, c, d, api_version='2')

def sendNotifications(text: str):
    '''Gets users emails and sends emails

    ############################################### '''
    
    if not sendSMS(text):
        print('Could not send mail to ')
    else:
        print('mail sent')
        
    return


def decideTwitter(text: str) -> bool:
    '''Returns true when matches the pattern of the text

    ############################################### '''
    
    return not not (pattern.search(text))


def analyseTwitter()->bool:
    '''Runs the analysis over the tweets
    ############################################### '''
    # get twets
    global lastTweet
    tweets = api.request('users/:{}/tweets'.format(twitterID),
                         {'max_results': numTweets})
    nextLast = None
    for idx, tw in enumerate(tweets):
        if idx == 0:
            nextLast = tw['id']
        if tw['id'] == lastTweet:
            print('Already checked, not checking anymore')
            break
        #else...
        # analysing!
        print('{}: {}'.format(idx, tw['text']))

        if decideTwitter(tw['text']):
            print('Is decided\n\n')
            sendNotifications(tw['text'])
            # maybe more than 1 tweet
    lastTweet = nextLast

    with open("p.pickle", "wb") as f:
        pickle.dump(lastTweet, f)
    return


