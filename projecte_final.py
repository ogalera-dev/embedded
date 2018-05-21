#!/usr/bin/env python
# importem la llibreria GPIO

import RPi.GPIO as GPIO, feedparser, time

import urllib2
import json
import time

import sys, locale, threading 
#import oauth, tweepy, sys, locale, threading 
from time import localtime, strftime, sleep


##################### Gmail

DEBUG = 1

USERNAME = "oga.mab123"     # just the part before the @ sign, add yours here
PASSWORD = "oga.mab123"

NEWMAIL_OFFSET = 1        # my unread messages never goes to zero, yours might

##################### Gmail

# configuracio per els ports GPIO
# utilitzarem la identificacio BCM per els ports GPIO
GPIO.setmode(GPIO.BCM)

SEG_A = 21
SEG_B = 20
SEG_C = 16
SEG_D = 12
SEG_E = 25
SEG_F = 24
SEG_G = 23

D2_SEG_A = 6
D2_SEG_B = 5
D2_SEG_C = 22
D2_SEG_D = 27
D2_SEG_E = 17
D2_SEG_F = 4
D2_SEG_G = 18

#LED_GROC = 6
LED_VERD = 13
LED_VERMELL = 19
LED_BLAU = 26

# indiquem els ports de sortida GPIO
#GPIO.setup(LED_GROC, GPIO.OUT) ## GPIO 6 com a sortida. Led GROC
GPIO.setup(LED_VERD, GPIO.OUT) ## GPIO 13 com a sortida. Led VERD
GPIO.setup(LED_VERMELL, GPIO.OUT) ## GPIO 19 com a sortida. Led VERMELL
GPIO.setup(LED_BLAU, GPIO.OUT) ## GPIO 26 com a sortida. Led BLAU

#Configuracio del primer digit
GPIO.setup(SEG_A, GPIO.OUT) ## GPIO 21 com a sortida. SEGMNENT A
GPIO.setup(SEG_B, GPIO.OUT) ## GPIO 20 com a sortida. SEGMNENT B
GPIO.setup(SEG_C, GPIO.OUT) ## GPIO 16 com a sortida. SEGMNENT C
GPIO.setup(SEG_D, GPIO.OUT) ## GPIO 12 com a sortida. SEGMNENT D
GPIO.setup(SEG_E, GPIO.OUT) ## GPIO 25 com a sortida. SEGMNENT E
GPIO.setup(SEG_F, GPIO.OUT) ## GPIO 24 com a sortida. SEGMNENT F
GPIO.setup(SEG_G, GPIO.OUT) ## GPIO 23 com a sortida. SEGMNENT G

#Configuracio del segon digit
GPIO.setup(D2_SEG_A, GPIO.OUT) ## GPIO 21 com a sortida. SEGMNENT A
GPIO.setup(D2_SEG_B, GPIO.OUT) ## GPIO 20 com a sortida. SEGMNENT B
GPIO.setup(D2_SEG_C, GPIO.OUT) ## GPIO 16 com a sortida. SEGMNENT C
GPIO.setup(D2_SEG_D, GPIO.OUT) ## GPIO 12 com a sortida. SEGMNENT D
GPIO.setup(D2_SEG_E, GPIO.OUT) ## GPIO 25 com a sortida. SEGMNENT E
GPIO.setup(D2_SEG_F, GPIO.OUT) ## GPIO 24 com a sortida. SEGMNENT F
GPIO.setup(D2_SEG_G, GPIO.OUT) ## GPIO 23 com a sortida. SEGMNENT G


def PRINT_DISPLAY(display, digito):
    INICIALIZAR_DISPLAY() # apaguem tots els segments
    # activem els segments segons el numero
    if digito== 0: # numero 0
        GPIO.output(SEG_A if display == 1 else D2_SEG_A, True) # segment a
        GPIO.output(SEG_B if display == 1 else D2_SEG_B, True) # segment b
        GPIO.output(SEG_C if display == 1 else D2_SEG_C, True) # segment c
        GPIO.output(SEG_D if display == 1 else D2_SEG_D, True) # segment d
        GPIO.output(SEG_E if display == 1 else D2_SEG_E, True) # segment e
        GPIO.output(SEG_F if display == 1 else D2_SEG_F, True) # segment f
    elif digito== 1: # numero 1
        GPIO.output(SEG_B if display == 1 else D2_SEG_B, True) # segment b
        GPIO.output(SEG_C if display == 1 else D2_SEG_C, True) # segment c
    elif digito== 2: # numero 2
        GPIO.output(SEG_A if display == 1 else D2_SEG_A, True) # segment a
        GPIO.output(SEG_B if display == 1 else D2_SEG_B, True) # segment b
        GPIO.output(SEG_D if display == 1 else D2_SEG_D, True) # segment d
        GPIO.output(SEG_E if display == 1 else D2_SEG_E, True) # segment e
        GPIO.output(SEG_G if display == 1 else D2_SEG_G, True) # segment g
    elif digito== 3: # numero 3
        GPIO.output(SEG_A if display == 1 else D2_SEG_A, True) # segment a
        GPIO.output(SEG_B if display == 1 else D2_SEG_B, True) # segment b
        GPIO.output(SEG_C if display == 1 else D2_SEG_C, True) # segment c
        GPIO.output(SEG_D if display == 1 else D2_SEG_D, True) # segment d
        GPIO.output(SEG_G if display == 1 else D2_SEG_G, True) # segment g
    elif digito== 4: # numero 4
        GPIO.output(SEG_B if display == 1 else D2_SEG_B, True) # segment b
        GPIO.output(SEG_C if display == 1 else D2_SEG_C, True) # segment c
        GPIO.output(SEG_F if display == 1 else D2_SEG_F, True) # segment f
        GPIO.output(SEG_G if display == 1 else D2_SEG_G, True) # segment g
    elif digito== 5: # numero 5
        GPIO.output(SEG_A if display == 1 else D2_SEG_A, True) # segment a
        GPIO.output(SEG_C if display == 1 else D2_SEG_C, True) # segment c
        GPIO.output(SEG_D if display == 1 else D2_SEG_D, True) # segment d
        GPIO.output(SEG_F if display == 1 else D2_SEG_F, True) # segment f
        GPIO.output(SEG_G if display == 1 else D2_SEG_G, True) # segment g
    elif digito== 6: # numero 6
        GPIO.output(SEG_A if display == 1 else D2_SEG_A, True) # segment a
        GPIO.output(SEG_C if display == 1 else D2_SEG_C, True) # segment c
        GPIO.output(SEG_D if display == 1 else D2_SEG_D, True) # segment d
        GPIO.output(SEG_E if display == 1 else D2_SEG_E, True) # segment e
        GPIO.output(SEG_F if display == 1 else D2_SEG_F, True) # segment f
        GPIO.output(SEG_G if display == 1 else D2_SEG_G, True) # segment g
    elif digito== 7: # numero 7
        GPIO.output(SEG_A if display == 1 else D2_SEG_A, True) # segment a
        GPIO.output(SEG_B if display == 1 else D2_SEG_B, True) # segment b
        GPIO.output(SEG_C if display == 1 else D2_SEG_C, True) # segment c
    elif digito== 8: # numero SEG_G
        GPIO.output(SEG_A if display == 1 else D2_SEG_A, True) # segment a
        GPIO.output(SEG_B if display == 1 else D2_SEG_B, True) # segment b
        GPIO.output(SEG_C if display == 1 else D2_SEG_C, True) # segment c
        GPIO.output(SEG_D if display == 1 else D2_SEG_D, True) # segment d
        GPIO.output(SEG_E if display == 1 else D2_SEG_E, True) # segment e
        GPIO.output(SEG_F if display == 1 else D2_SEG_F, True) # segment f
        GPIO.output(SEG_G if display == 1 else D2_SEG_G, True) # segment g
    elif digito== 9: # numero 9
        GPIO.output(SEG_A if display == 1 else D2_SEG_A, True) # segment a
        GPIO.output(SEG_B if display == 1 else D2_SEG_B, True) # segment b
        GPIO.output(SEG_C if display == 1 else D2_SEG_C, True) # segment c
        GPIO.output(SEG_D if display == 1 else D2_SEG_D, True) # segment d
        GPIO.output(SEG_F if display == 1 else D2_SEG_F, True) # segment f
        GPIO.output(SEG_G if display == 1 else D2_SEG_G, True) # segment g

#inicialitzem a 0
def INICIALIZAR_DISPLAY():
    GPIO.output(SEG_A, False) # segment a
    GPIO.output(SEG_B, False) # segment b
    GPIO.output(SEG_C, False) # segment c
    GPIO.output(SEG_D, False) # segment d
    GPIO.output(SEG_E, False) # segment e
    GPIO.output(SEG_F, False) # segment f
    GPIO.output(SEG_G, False) # segment g

def INICIALITZAR_LEDS():
#    GPIO. output(LED_GROC, False)
    GPIO. output(LED_VERD, False)
    GPIO. output(LED_VERMELL, False)
    GPIO. output(LED_BLAU, False)

def gmail():
    global mail
    newmails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])
    print "You have", newmails, "new emails"
    mail = newmails

def get_page_data(page_id,access_token):
    api_endpoint = "https://graph.facebook.com/v2.4/"
    fb_graph_url = api_endpoint+page_id+"?fields=id,name,likes,unread_notif_count,unread_message_count,link&access_token="+access_token
    try:
        api_request = urllib2.Request(fb_graph_url)
        api_response = urllib2.urlopen(api_request)
        
        try:
            return json.loads(api_response.read())
        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except IOError, e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason
            
def facebook():
    #global like_count
    global notification_count
    page_id = "176830336311921" 
    # username or id <a href="https://developers.facebook.com/tools/explorer"> https://developers.facebook.com/tools/explorer</a>

    token = "EAACEdEose0cBADnZCzLCgTFTRPKBVklGey1wZCEB4JzCX3ggv46HZAKzggZCTQtXZBqUtgutZBXnvKHIY6RoYmkl11ZC3LeKkYIL4FCKy7ewlzbnZBq6UcKTHOYZAOXuCjBnyX5H828kw9TbEnSzgXUZAu3a5CzZAZBLfgkEfsqwuV3wKB8qJJfudUfBwuULWmCfSqfLkWgVJZAzQPBxKZC4tZCfsxT"  # Access Token
    page_data = get_page_data(page_id,token)

    print "Page Name:"+ page_data['name']
    #print "Likes:"+ str(page_data['likes'])
    #like_count = page_data['likes']
    print "Link:"+ page_data['link']
    print "Unread notifications:"+ str(page_data['unread_notif_count'])
    notification_count = page_data['unread_notif_count']
    print "Unread message:"+ str(page_data['unread_message_count'])

    #time.sleep(0.5)

def twitter(): 
    global follower
    global api    #https://apps.twitter.com
    consumer_key = "xxxxxxxxxxxxxxxxxxxxxx"  # use your access key
    consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxx"
    access_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    access_secret = "xxxxxxxxxxxxxxxxxxxxxxxxx"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    user = api.get_user(xxxxxxxxxx)  # your user id
    print user.screen_name
    print user.followers_count
    follower = user.followers_count
    print user.friends_count
    print user.favourites_count
        
def reverse(n):
    if(n<10):
        return PRINT_DISPLAY(1, all_value)
    else:
        return PRINT_DISPLAY(2,int(str(n)[::-1]))

while 1:
    ############################# GMAIL #############################
    INICIALIZAR_DISPLAY()
    #Inicialitzem els Leds
    INICIALITZAR_LEDS()

    # ENCENEM EL LED VERMELL
    GPIO.output(LED_VERMELL, 1)

    # CONSULTEM EL GMAIL
    gmail()

    # IMPRIMIM EL NUMERO QUE HEM REBUT
    all_value = mail

    PRINT_DISPLAY(1, all_value)
    #reverse(all_value)

    # ESPEREM 5 SEGONS
    time.sleep(10)

    ############################# FACEBOOK #############################
    INICIALIZAR_DISPLAY()
    #Inicialitzem els Leds
    INICIALITZAR_LEDS()

    # ENCENEM EL LED BLAU
    GPIO.output(LED_BLAU, 1)
    # CONSULTEM EL FACEBOOK
    facebook()

    # IMPRIMIM EL NUMERO QUE HEM REBUT
    all_value = notification_count
    PRINT_DISPLAY(1, all_value)

    # ESPEREM 5 SEGONS
    time.sleep(10)
