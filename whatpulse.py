# whatpulse.py
# this file is part of hexchat-pyscripts
#
# whatpulse spammer
#
# written by and copyright (C) Erica Garcia [athenaorerica] <me@athenas.space> 2019
# licensed under the MIT license [https://mit.athenas.space]
#
# this code says: trans rights
#
# don't like the previous statement? suck it up, or write your own code. ^-^

import requests
import hexchat
import threading

__module_name__ = 'whatpulse spam'
__module_description__ = 'spams whatpulse'
__module_version__ = '0.0.3a'
__author__ = 'Erica Garcia [athenaorerica] <me@athenas.space>'

wpUsername = "ApolloJustice"

def getData(chan):
	wpData = requests.get("http://api.whatpulse.org/user.php?user={}&format=json".format(wpUsername)).json()
	spamString = "WhatPulse Stats for \002\00302{}\017 | Keys: \002\00302{}\017 (Rank \002\00302{}\017) | Clicks: \002\00302{}\017 (Rank \002\00302{}\017) | DL: \002\00302{}\017 (Rank \002\00302{}\017) | UL: \002\00302{}\017 (Rank \002\00302{}\017) | Uptime: \002\00302{}\017 (Rank \002\00302{}\017) | Avg. Keys/s \002\00302{}\017 | Avg. Clicks/s \002\00302{}\017".format(wpData['AccountName'], wpData['Keys'], wpData['Ranks']['Keys'], wpData['Clicks'], wpData['Ranks']['Clicks'], wpData['Download'], wpData['Ranks']['Download'], wpData['Upload'], wpData['Ranks']['Upload'], wpData['UptimeShort'], wpData['Ranks']['Uptime'], wpData['AvKPS'], wpData['AvCPS'])
	hexchat.command("msg {} {}".format(chan, spamString))

def spamWP(word, word_eol, userdata):
	chan = hexchat.get_info('channel')
	dataThread = threading.Thread(target=getData, kwargs={"chan": chan})
	dataThread.start()
	return hexchat.EAT_ALL	

hexchat.hook_command("whatpulse", spamWP)
