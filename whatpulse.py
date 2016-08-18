# whatpulse.py by ApolloJustice
# for use with Python 3
# non PEP-8 compliant because honestly fuck that
# probably not commented because too lazy

import requests, hexchat, threading

__module_name__ = 'whatpulse spam'
__module_description__ = 'spams whatpulse'
__module_version__ = '0.0.1a'
__author__ = 'ApolloJustice'

wpUsername = "ApolloJustice"

def getData():
	wpData = requests.get("http://api.whatpulse.org/user.php?user={}&format=json".format(wpUsername)).json()
	spamString = "WhatPulse Stats for \002\00302{}\017 | Keys: \002\00302{}\017 (Rank \002\00302{}\017) | Clicks: \002\00302{}\017 (Rank \002\00302{}\017) | DL: \002\00302{}\017 (Rank \002\00302{}\017) | UL: \002\00302{}\017 (Rank \002\00302{}\017) | Uptime: \002\00302{}\017 (Rank \002\00302{}\017) | Avg. Keys/s \002\00302{}\017 | Avg. Clicks/s \002\00302{}\017".format(wpData['AccountName'], wpData['Keys'], wpData['Ranks']['Keys'], wpData['Clicks'], wpData['Ranks']['Clicks'], wpData['Download'], wpData['Ranks']['Download'], wpData['Upload'], wpData['Ranks']['Upload'], wpData['UptimeShort'], wpData['Ranks']['Uptime'], wpData['AvKPS'], wpData['AvCPS'])
	hexchat.command("say {}".format(spamString))

def spamWP(word, word_eol, userdata):
	dataThread = threading.Thread(target=getData)
	dataThread.start()
	return hexchat.EAT_ALL

hexchat.hook_command("whatpulse", spamWP)
