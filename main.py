#!/usr/bin/env python
#
# LCS Twitter Tracker
# written by Lemonilla NA
#
# Tweets when:
#       ~playerName~ earns kill on ~playerName~
#       ~teamName~ kills Dragon
#       ~teamName~ kills Baron
#       ~teamName~ destroys tower (xxx#)
#               bot/mid/top/nex #/i
#       ~teamName~ wins

import twitter
import sys
import requests
import json

