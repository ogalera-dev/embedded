#!/usr/bin/env python
# importem la llibreria GPIO

import sys, locale, threading 
import oauth, tweepy, sys, locale, threading 
from time import localtime, strftime, sleep

def twitter(): 
    global follower
    global api    #https://apps.twitter.com
    consumer_key = "6Ov9ZYpGrYfCv3xomagiPEWB8"  # use your access key
    consumer_secret = "SZkb5GyBnWw0O8DjaQ0dFhnHSoQXXEo1NQfIsWbNryNhVPlbtl"
    access_key = "  998955377575251968-5VT2GrKdrNLavQlZwzdzIUc104wttUK"
    access_secret = "7b6hHVpTA2ZVM61OL5ntSb5uImjOJ9lBSA9RDsxB155Xd"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    user = api.get_user(998955377575251968)  # your user id
    print "Usuari: " + user.screen_name
    print "Followers " + user.followers_count
    follower = user.followers_count
    print "Friends " + user.friends_count
    print "Favourites " + user.favourites_count

twitter();
