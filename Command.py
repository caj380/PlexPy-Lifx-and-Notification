import os
import sys
import lazylights
from colour import Color
import binascii
import time
import requests


#------------------------------------------------------------------------------------------------------------
# I use this to manually create a bulb using IP and MAC address. 
def createBulb(ip, macString, port = 56700):        
    return lazylights.Bulb(b'LIFXV2', binascii.unhexlify(macString.replace(':', '')), (ip,port))
#------------------------------------------------------------------------------------------------------------	

Theater = createBulb('192.168.1.xxx','xx:xx:xx:xx:xx:xx')  #Bulb for Theater room
bulbs=[Theater]

status = sys.argv[1]
user = sys.argv[2]
action = sys.argv[3]
media = sys.argv[4]
#print status

if (status =="My SHIELD Android TV" or status =="SHIELD Android TV"):
    if (action =="Play" or action =="Resume"):
        c = Color("#FFB87B")
        lazylights.set_state(bulbs,c.hue*360,(0),0.2,3199,(1000),False);
        print "Dim"

    if (action =="Pause" or action =="Stop"):
        c = Color("#FFB87B")
        lazylights.set_state(bulbs,c.hue*360,(0),0.35,3199,(1000),False);
        print "Bright"

USERNAME = 'tbmx12'  # Your username to filter out

if (user == USERNAME and action =="Play" and (status =="Jon.g" or status =="XboxOne")):
    
    NOTIFY_BODY = (user + " has started watching: " + media)
    PLEXPY_URL = 'http://localhost:8181/'  # Your PlexPy URL
    PLEXPY_APIKEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # Enter your PlexPy API Key
    AGENT_ID = 18  # The PlexPy notifier agent id found here: https://github.com/dr$
    NOTIFY_SUBJECT = 'PlexPy'  # The notification subject
    # Send notification to PlexPy using the API
    payload = {'apikey': PLEXPY_APIKEY,
               'cmd': 'notify',
               'agent_id': AGENT_ID,
               'subject': NOTIFY_SUBJECT,
               'body': NOTIFY_BODY,
               'notify_action': action.lower()}

    r = requests.post(PLEXPY_URL.rstrip('/') + '/api/v2', params=payload)
else:
    pass
