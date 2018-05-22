import urllib2
import json
import time

def get_page_data(page_id,access_token):
    api_endpoint = "https://graph.facebook.com/v2.4/"
    fb_graph_url = api_endpoint+page_id+"?fields=id,name,likes,unread_notif_count,link&access_token="+access_token
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
                                    
while 1:
    page_id = "176830336311921" # username or id 
    token = "EAACEdEose0cBAGc8X4aAwZAIXbW2lTKYwRzvMunqFAIOcLUC2VTd9FcscCxVGiKyuP1anJ5WeU6v65yZCzymOaSNxjvGisZCkusZAeZBGvRjCdIvTigTayvO5ZCyurQZA7L0l1UaPdbJZBzHRo6Sle5uaPZCcKY0tzAZB52fZBRwNoLjcIlI1KsdNgMREMz8726GmkuoT6uDbnczZBxok0FxXz1X"  # Access Token
    page_data = get_page_data(page_id,token)

    print "Nom:"+ page_data['name']
    print "Link:"+ page_data['link']
    print "Notificacions no llegides:"+ str(page_data['unread_notif_count'])
    notification_count = page_data['unread_notif_count']
    print "Missatges no llegits:"+ str(page_data['unread_message_count'])
    
    time.sleep(0.5)