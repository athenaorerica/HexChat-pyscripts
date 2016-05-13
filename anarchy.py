# anarchy.py by ApolloJustice
# for use with Python 3
# non PEP-8 compliant because honestly fuck that
# probably not commented because too lazy

__module_name__ = "Anarchizer"
__module_version__ = "1.0"
__module_description__ = "Makes a channel into an ANARCHY"
__author__ = "ApolloJustice"

import hexchat

def anarchize(word, word_eol, userdata):
	chan = hexchat.get_info("channel")
	
	if len(word) == 1:
		print("Are you sure? Type /anarchy confirm to make %s into an anarchy." % chan)
		return hexchat.EAT_ALL
	if word[1] != 'confirm':
		print("Are you sure? Type /anarchy confirm to make %s into an anarchy." % chan)
		return hexchat.EAT_ALL
	if word[1] == 'confirm':
		userlist = []
		for i in hexchat.get_list('users'):
			userlist.append(i.nick.lower())
		UList = ' '.join(map(str, userlist)) 
		hexchat.command("me declares %s an anarchy!" % chan)
		hexchat.command("cs op %s" % chan)
		hexchat.command("timer 2 op %s" % UList)
		return hexchat.EAT_ALL
		
hexchat.hook_command("anarchy", anarchize)

hexchat.emit_print('Notice', __module_name__ + ' [S]', '%s by %s loaded. You are using version %s of the script.' % (__module_name__, __author__, __module_version__))