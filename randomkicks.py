# randomkicks.py by ApolloJustice
# for use with Python 3
# non PEP-8 compliant because honestly fuck that
# probably not commented because too lazy

__module_name__ = "RandomKicks"
__module_version__ = "0.3.4b"
__module_description__ = "Adds a random message to kicks from a file."
__author__ = "ApolloJustice"

import hexchat as hexchat
import random

textfiledir = hexchat.get_info("configdir")

def kbquote(word, word_eol, userdata):
	if len(word) <= 1:
		hexchat.emit_print("Notice", __module_name__, "No arguments given.")
		return hexchat.EAT_ALL

	nick = hexchat.get_info("nick")
	chan = hexchat.get_info("channel")
	userlist = hexchat.get_list("users")
	
	try: line = random.choice(open(textfiledir + "\quotes.txt", "r").readlines())
	except:
		hexchat.emit_print("Notice", __module_name__ + " [S]", "Failed to grab a line from quotes.txt (Make sure it's in your config folder!), Using default reason if reason was not specified.")
		line = "No reason specified."

	for user in userlist:
		if user.nick.lower() == word[1].lower(): break

	host = user.host.partition('@')[2]

	if user.nick.lower() == word[1].lower():	
		hexchat.command("raw mode " + chan + " +b *!*@" + host)

	else:
		hexchat.emit_print("Notice", __module_name__ + " [S]", "User not found.")
		return hexchat.EAT_ALL

	try: reason = word_eol[2]
	except: reason = line

	reason = reason.replace('\n', '').replace('\r', '').replace('%k', word[1]).replace('%c', chan).replace('%u', nick)
	hexchat.command("raw kick  " + chan + " " + word[1] + " " + ":" + reason + " [Banned]")

	return hexchat.EAT_ALL

def kickquote(word, word_eol, userdata):
	if len(word) <= 1:
		hexchat.emit_print("Notice", __module_name__, "No arguments given.")
		return hexchat.EAT_ALL
	
	nick = hexchat.get_info("nick")
	chan = hexchat.get_info("channel")
	userlist = hexchat.get_list("users")
	try: line = random.choice(open(textfiledir + "\quotes.txt", "r").readlines())
	except:
		hexchat.emit_print("Notice", __module_name__ + " [S]", "Failed to grab a line from quotes.txt (Make sure it's in your config folder!)-- Using default reason if reason was not specified.")
		line = "No reason specified."

	try: reason = word_eol[2]
	except IndexError: reason = line

	for user in userlist:
		if user.nick.lower() == word[1].lower(): break

	reason = reason.replace('\n', '').replace('\r', '').replace('%k', word[1]).replace('%c', chan).replace('%u', nick)
	if user.nick.lower() == word[1].lower():
		hexchat.command("raw kick  " + chan + " " + word[1] + " " + ":" + reason)

	else: hexchat.emit_print("Notice", __module_name__ + " [S]", "User not found.")
	return hexchat.EAT_ALL

hexchat.hook_command("kick", kickquote, help="/kick Kicks a user.")
hexchat.hook_command("kickban", kbquote, help="/kickban Kicks and bans a user.")
hexchat.emit_print("Notice", __module_name__ + " [S]", "%s by %s loaded. You are using version %s of the script." % (__module_name__, __author__, __module_version__))
