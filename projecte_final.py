#!/usr/bin/env python
# importem la llibreria GPIO

import RPi.GPIO as GPIO, feedparser, time

import urllib2
import json
import time

import sys, locale, threading 
#import oauth, tweepy, sys, locale, threading 
from time import localtime, strftime, sleep

import tweepy


##################### Gmail

DEBUG = 1

USERNAME = "oga.mab123"     # just the part before the @ sign, add yours here
PASSWORD = "oga.mab123"

NEWMAIL_OFFSET = 1        # my unread messages never goes to zero, yours might

DELAY_REFRESC_S = 7

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

D2_SEG_A = 06
D2_SEG_B = 05
D2_SEG_C = 22
D2_SEG_D = 27
D2_SEG_E = 17
D2_SEG_F=4
D2_SEG_G = 18

#LED_GROC = 6
LED_VERD = 13
LED_VERMELL = 19
LED_BLAU = 26

# indiquem els ports de sortida GPIO
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
    elif digito== 8: # numero 8
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
    GPIO.output(D2_SEG_F, True)

#inicialitzem a 0
def INICIALIZAR_DISPLAY():
    GPIO.output(SEG_A, False) # segment a
    GPIO.output(SEG_B, False) # segment b
    GPIO.output(SEG_C, False) # segment c
    GPIO.output(SEG_D, False) # segment d
    GPIO.output(SEG_E, False) # segment e
    GPIO.output(SEG_F, False) # segment f
    GPIO.output(SEG_G, False) # segment g
    GPIO.output(D2_SEG_A, False) # segment a
    GPIO.output(D2_SEG_B, False) # segment b
    GPIO.output(D2_SEG_C, False) # segment c
    GPIO.output(D2_SEG_D, False) # segment d
    GPIO.output(D2_SEG_E, False) # segment e
    GPIO.output(D2_SEG_F, False) # segment f
    GPIO.output(D2_SEG_G, False) # segment g

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

    token = "EAACEdEose0cBAGc8X4aAwZAIXbW2lTKYwRzvMunqFAIOcLUC2VTd9FcscCxVGiKyuP1anJ5WeU6v65yZCzymOaSNxjvGisZCkusZAeZBGvRjCdIvTigTayvO5ZCyurQZA7L0l1UaPdbJZBzHRo6Sle5uaPZCcKY0tzAZB52fZBRwNoLjcIlI1KsdNgMREMz8726GmkuoT6uDbnczZBxok0FxXz1X"  # Access Token
    page_data = get_page_data(page_id,token)

    print "Nom:"+ page_data['name']
    print "Link:"+ page_data['link']
    print "Notificacions no llegides:"+ str(page_data['unread_notif_count'])
    notification_count = page_data['unread_notif_count']
    print "Missatges no llegits:"+ str(page_data['unread_message_count'])

    #time.sleep(0.5)

def twitter(): 
    global follower
    global api    #https://apps.twitter.com
    consumer_key = "6Ov9ZYpGrYfCv3xomagiPEWB8"  # use your access key
    consumer_secret = "SZkb5GyBnWw0O8DjaQ0dFhnHSoQXXEo1NQfIsWbNryNhVPlbtl"
    access_key = "998955377575251968-5VT2GrKdrNLavQlZwzdzIUc104wttUK"
    access_secret = "7b6hHVpTA2ZVM61OL5ntSb5uImjOJ9lBSA9RDsxB155Xd"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    user = api.get_user('998955377575251968')  # your user id
    follower = user.followers_count


# CONSULTEM EL GMAIL
gmail()
while 1:
    ############################# GMAIL #############################
    INICIALIZAR_DISPLAY()
    #Inicialitzem els Leds
    INICIALITZAR_LEDS()

    # ENCENEM EL LED VERMELL
    GPIO.output(LED_VERMELL, 1)

    # CONSULTEM EL GMAIL
    # IMPRIMIM EL NUMERO QUE HEM REBUT
    all_value = mail

    #Primer digit del gmail
    PRINT_DISPLAY(1, int(all_value%10))

    all_value = all_value/10
    #Segon digit del gmail
    PRINT_DISPLAY(2, all_value if all_value < 10 else 9)

    #reverse(all_value)

    # ESPEREM
    time.sleep(DELAY_REFRESC_S)

    ############################# FACEBOOK #############################
    facebook()
    INICIALIZAR_DISPLAY()
    #Inicialitzem els Leds
    INICIALITZAR_LEDS()

    # ENCENEM EL LED BLAU
    GPIO.output(LED_BLAU, 1)
    # CONSULTEM EL FACEBOOK

    # IMPRIMIM EL NUMERO QUE HEM REBUT
    all_value = notification_count
    #all_value = 0
    PRINT_DISPLAY(1, all_value%10)
    all_value = all_value/10
    PRINT_DISPLAY(2, all_value if all_value < 10 else 9)

    # ESPEREM
    time.sleep(DELAY_REFRESC_S)

    ############################# TWITTER #############################
    twitter()
    INICIALIZAR_DISPLAY()
    #Inicialitzem els Leds
    INICIALITZAR_LEDS()

    # ENCENEM EL LED BLAU
    GPIO.output(LED_VERD, 1)

    # IMPRIMIM EL NUMERO QUE HEM REBUT
    #all_value = notification_count
    all_value = follower
    PRINT_DISPLAY(1, all_value%10)
    all_value = all_value/10
    PRINT_DISPLAY(2, all_value if all_value < 10 else 9)

    # ESPEREM
    time.sleep(DELAY_REFRESC_S)

    #CONSULTA GMAIL
    gmail()
