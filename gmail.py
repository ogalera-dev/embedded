
#!/usr/bin/env python

import RPi.GPIO as GPIO, feedparser, time

DEBUG = 1

USERNAME = "oga.mab123"     # just the part before the @ sign, add yours here
PASSWORD = "oga.mab123"   

NEWMAIL_OFFSET = 1        # my unread messages never goes to zero, yours might
MAIL_CHECK_FREQ = 60      # check mail every 60 seconds

while True:

        newmails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])

        if DEBUG:
                print("You have", newmails, "new emails!")

        
        time.sleep(MAIL_CHECK_FREQ)
