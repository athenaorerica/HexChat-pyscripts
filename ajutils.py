# ajutils.py by ApolloJustice
# for use with Python 3
# non PEP-8 compliant because honestly fuck that
# probably not commented because too lazy

__module_name__ = 'AJUtils'
__module_version__ = '1.0'
__module_description__ = 'General commands.'
__author__ = 'ApolloJustice'

zncPrefix = '*'

import hexchat

def nea():
	hexchat.emit_print('Notice', '%s [S]' % __module_name__, 'No arguments given.')
	
def unf():
	hexchat.emit_print('Notice', '%s [S]' % __module_name__, 'User not found.')

def getHost(uList, target):
	for user in uList:
		if user.nick.lower() == target.lower(): break
	
	return user

def clearstatus(word, word_eol, userdata):
	anyLeft = 1
	while anyLeft == 1:
		try:
			statusContexts = hexchat.find_context(channel='{0}status'.format(zncPrefix))
			statusContexts.command("close")
		except AttributeError:
			anyLeft = 0
	return hexchat.EAT_ALL

def disablechan(word, word_eol, userdata):
	chan = hexchat.get_info('channel')
	action = userdata
	if action == "disabled": hexchat.command('RAW PRIVMSG *status :disablechan %s' % chan)
	if len(word) == 1:
		hexchat.command('raw PART %s' % chan)
	elif len(word) >= 2:
		hexchat.command('raw PART %s :%s' % (chan, word_eol[1]))
	hexchat.emit_print('Notice', '%s [S]' % __module_name__, 'Parted %s and %s it in ZNC.' % (chan, action))
	return hexchat.EAT_ALL

def sudo(word, word_eol, userdata):
	if len(word) <= 1: 
		nea()
		return hexchat.EAT_ALL
	
	chan = hexchat.get_info('channel')
	cmd = word_eol[1]
	
	hexchat.command('RAW PRIVMSG ChanServ :op %s' % chan)
	hexchat.command('timer 1 %s' % cmd)
	hexchat.command('timer 1.7 RAW PRIVMSG ChanServ :deop %s' % chan)
	return hexchat.EAT_ALL

def topicappend(word, word_eol, userdata):
	oldtopic = hexchat.get_info('topic')
	newtopic = '%s | %s' % (oldtopic.rstrip(), word_eol[1])
	
	if len(word) <= 1: 
		nea()
		return hexchat.EAT_ALL
		
	hexchat.command('topic %s' % newtopic)
	return hexchat.EAT_ALL
	
def hostignore(word, word_eol, userdata):
	userlist = hexchat.get_list('users')
	action = userdata
	
	if len(word) <= 1: 
		nea()
		return hexchat.EAT_ALLs
		
	user = getHost(userlist, word[1])
	host = user.host.split('@')[1]
	
	if user.nick.lower() == word[1].lower(): hexchat.command('%s *!*@%s' % (action, host))
	else: unf()
	
	return hexchat.EAT_ALL
	
def hostMode(word, word_eol, userdata):
	userlist = hexchat.get_list('users')
	mode = userdata
	
	if len(word) <= 1: 
		nea()
		return hexchat.EAT_ALL
	
	if any(ext in word[1] for ext in ["@", "$", ":"]):
		hexchat.command('raw MODE %s %s %s' % (hexchat.get_info('channel'), mode, word[1]))
		return hexchat.EAT_ALL
	
	user = getHost(userlist, word[1])
	host = user.host.split('@')[1]
	
	if user.nick.lower() == word[1].lower(): hexchat.command('raw MODE %s %s *!*@%s' % (hexchat.get_info('channel'), mode, host))
	else: unf()
	
	return hexchat.EAT_ALL
	
def editflags(word, word_eol, userdata):
	if len(word) <= 1:
		hexchat.command('msg chanserv access ' + hexchat.get_info('channel') + ' list')
		return hexchat.EAT_ALL
		
	if '#' not in word[1]: hexchat.command('msg chanserv flags ' + hexchat.get_info('channel') + ' ' + word_eol[1])
	if '#' in word[1]: hexchat.command('msg chanserv flags ' + word_eol[1])
	return hexchat.EAT_ALL
	
def showver(word, word_eol, userdata):
	hexchat.command('me is using HexChat v%s' % hexchat.get_info('version'))
	return hexchat.EAT_ALL
	
hexchat.hook_command('sudo', sudo, help='/sudo Executes a command as op on channels you have flag +o on.')
hexchat.hook_command('topicappend', topicappend, help='/topicappend Adds a string to the topic')
hexchat.hook_command('appendtopic', topicappend, help='/appendtopic Adds a string to the topic')
hexchat.hook_command('part', disablechan, userdata="disabled", help='/part parts and disables chan on znc')
hexchat.hook_command('temppart', disablechan, userdata="did not disable", help='/temppart parts without disabling chan on znc')
hexchat.hook_command('ignorehost', hostignore, userdata="ignore", help='/ignorehost ignores a user\'s host')
hexchat.hook_command('unignorehost', hostignore, userdata="unignore", help='/unignorehost ignores a user\'s host')
hexchat.hook_command('quiet', hostMode, userdata="+q", help='/quiet quiets a user')
hexchat.hook_command('unquiet', hostMode, userdata="-q", help='/unquiet unquiets a user')
hexchat.hook_command('iexempt', hostMode, userdata="+I", help='/exempt adds an invite exemption for a user')
hexchat.hook_command('uniexempt', hostMode, userdata="-I", help='/unexempt removes an invite exemption for a user')
hexchat.hook_command('exempt', hostMode, userdata="+e", help='/exempt adds a ban exemption for a user')
hexchat.hook_command('unexempt', hostMode, userdata="-e", help='/unexempt removes a ban exemption for a user')
hexchat.hook_command('flags', editflags, help='/flags edits chanserv flags for a user')
hexchat.hook_command('clearstatus', clearstatus, help='/clearstatus closes all ZNC status windows. You can set your prefix at the top of the python file')
hexchat.hook_command('showver', showver)

hexchat.emit_print('Notice', __module_name__ + ' [S]', '%s by %s loaded. You are using version %s of the script.' % (__module_name__, __author__, __module_version__))