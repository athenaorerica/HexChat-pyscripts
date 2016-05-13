# chanmsg.py by ApolloJustice
# for use with Python 3
# non PEP-8 compliant because honestly fuck that
# probably not commented because too lazy

__module_name__ = "ChanMsg"
__module_version__ = "1.0"
__module_description__ = "Messages an array of channels"
__author__ = "ApolloJustice"

import hexchat

def chanmsg(word, word_eol, userdata):
	chanstr = word[1].split(",")
	for chan in chanstr: hexchat.find_context(channel=chan).command("say " + word_eol[2])
	return hexchat.EAT_ALL
	
hexchat.hook_command("chanmsg", chanmsg)
hexchat.emit_print("Notice", __module_name__ + " [Plugin]", "%s by %s loaded. You are using version %s of the script." % (__module_name__, __author__, __module_version__))