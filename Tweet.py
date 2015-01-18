#!/usr/bin/env python
#############################################################################################################################################
# Introduction: 	This script will post a Tweet to Twitter.
# 					You need to input your CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY and ACCESS_SECRET values.
#					For more information, see here: http://allynh.com/blog/making-a-twitter-bot-on-your-galileo-or-raspberry-pi/
#
# Usage: 			python Tweet.py "Hello world!"
# Syntax: 			python Tweet.py "<Your text here...>"
#
# Output:			Output is posted to Twitter.
# Version: 			V1.0
# Owner:			Allyn H
#					www.AllynH.com
#############################################################################################################################################

import sys
from twython import Twython

CONSUMER_KEY = '<YOUR CONSUMER_KEY>'
CONSUMER_SECRET = '<YOUR CONSUMER_SECRET>'
ACCESS_KEY = '<YOUR ACCESS_KEY>'
ACCESS_SECRET = '<YOUR ACCESS_SECRET>'

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

twitter.update_status(status=sys.argv[1][:140])

