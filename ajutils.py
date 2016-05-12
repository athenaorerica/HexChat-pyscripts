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
	
	hexchat.command('RAW PRIVMSG *status :disablechan %s' % chan)
	if len(word) == 1:
		hexchat.command('raw PART %s' % chan)
	elif len(word) >= 2:
		hexchat.command('raw PART %s :%s' % (chan, word_eol[1]))
	hexchat.emit_print('Notice', '%s [S]' % __module_name__, 'Parted %s and disabled it in ZNC.' % chan)
	return hexchat.EAT_ALL

def temppart(word, word_eol, userdata):
	chan = hexchat.get_info('channel')
	if len(word) == 1:
		hexchat.command('raw PART %s' % chan)
	elif len(word) >= 2:
		hexchat.command('raw PART %s :%s' % (chan, word_eol[1]))
		
	hexchat.emit_print('Notice', '%s [S]' % __module_name__, 'Parted %s without disabling it in ZNC.' % chan)
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
	
	if len(word) <= 1: 
		nea()
		return hexchat.EAT_ALL

	for user in userlist:
		if user.nick.lower() == word[1].lower(): break
		
	host = user.host.split('@')[1]
	
	if user.nick.lower() == word[1].lower(): hexchat.command('ignore *!*@%s' % host)
	else: unf()
	
	return hexchat.EAT_ALL
	
def hostunignore(word, word_eol, userdata):
	userlist = hexchat.get_list('users')
	
	if len(word) <= 1: 
		nea()
		return hexchat.EAT_ALL

	for user in userlist:
		if user.nick.lower() == word[1].lower(): break
		
	host = user.host.split('@')[1]
	
	if user.nick.lower() == word[1].lower(): hexchat.command('unignore *!*@%s' % host)
	else: unf()
	
	return hexchat.EAT_ALL
	
def quiet(word, word_eol, userdata):
	userlist = hexchat.get_list('users')
	
	if len(word) <= 1: 
		nea()
		return hexchat.EAT_ALL
		
	for user in userlist:
		if user.nick.lower() == word[1].lower(): break
	
	host = user.host.split('@')[1]
	
	if '@' in word[1] or '$' in word[1] or ':' in word[1]:
		hexchat.command('raw MODE %s +q %s' % (hexchat.get_info('channel'), word[1]))
		return hexchat.EAT_ALL
	
	if user.nick.lower() == word[1].lower(): hexchat.command('raw MODE %s +q *!*@%s' % (hexchat.get_info('channel'), host))
	else: unf()
	
	return hexchat.EAT_ALL
	
def unquiet(word, word_eol, userdata):
	userlist = hexchat.get_list('users')
	
	if len(word) <= 1: 
		nea()
		return hexchat.EAT_ALL
		
	for user in userlist:
		if user.nick.lower() == word[1].lower(): break
	
	host = user.host.split('@')[1]
	
	if '@' in word[1] or '$' in word[1] or ':' in word[1]:
		hexchat.command('raw MODE %s -q %s' % (hexchat.get_info('channel'), word[1]))
		return hexchat.EAT_ALL
	
	if user.nick.lower() == word[1].lower(): hexchat.command('raw MODE %s -q *!*@%s' % (hexchat.get_info('channel'), host))
	else: unf()
	
	return hexchat.EAT_ALL

def exempt(word, word_eol, userdata):
	userlist = hexchat.get_list('users')
	
	if len(word) <= 1: 
		nea()
		return hexchat.EAT_ALL
		
	for user in userlist:
		if user.nick.lower() == word[1].lower(): break
	
	host = user.host.split('@')[1]
	
	if '@' in word[1] or '$' in word[1] or ':' in word[1]:
		hexchat.command('raw MODE %s +e %s' % (hexchat.get_info('channel'), word[1]))
		return hexchat.EAT_ALL
	
	if user.nick.lower() == word[1].lower(): hexchat.command('raw MODE %s +e *!*@%s' % (hexchat.get_info('channel'), host))
	else: unf()
	
	return hexchat.EAT_ALL
	
def unexempt(word, word_eol, userdata):
	userlist = hexchat.get_list('users')
	
	if len(word) <= 1: 
		nea()
		return hexchat.EAT_ALL
		
	for user in userlist:
		if user.nick.lower() == word[1].lower(): break
	
	host = user.host.split('@')[1]
	
	if '@' in word[1] or '$' in word[1] or ':' in word[1]:
		hexchat.command('raw MODE %s -e %s' % (hexchat.get_info('channel'), word[1]))
		return hexchat.EAT_ALL
	
	if user.nick.lower() == word[1].lower(): hexchat.command('raw MODE %s -e *!*@%s' % (hexchat.get_info('channel'), host))
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

def inviteexempt(word, word_eol, userdata):
	userlist = hexchat.get_list('users')
	
	if len(word) <= 1: 
		nea()
		return hexchat.EAT_ALL
		
	for user in userlist:
		if user.nick.lower() == word[1].lower(): break
	
	host = user.host.split('@')[1]
	
	if '@' in word[1] or '$' in word[1] or ':' in word[1]:
		hexchat.command('raw MODE %s +I %s' % (hexchat.get_info('channel'), word[1]))
		return hexchat.EAT_ALL
	
	if user.nick.lower() == word[1].lower(): hexchat.command('raw MODE %s +I *!*@%s' % (hexchat.get_info('channel'), host))
	else: unf()
	
	return hexchat.EAT_ALL
	
def uninviteexempt(word, word_eol, userdata):
	userlist = hexchat.get_list('users')
	
	if len(word) <= 1: 
		nea()
		return hexchat.EAT_ALL
		
	for user in userlist:
		if user.nick.lower() == word[1].lower(): break
	
	host = user.host.split('@')[1]
	
	if '@' in word[1] or '$' in word[1] or ':' in word[1]:
		hexchat.command('raw MODE %s -I %s' % (hexchat.get_info('channel'), word[1]))
		return hexchat.EAT_ALL
	
	if user.nick.lower() == word[1].lower(): hexchat.command('raw MODE %s -I *!*@%s' % (hexchat.get_info('channel'), host))
	else: unf()
	
	return hexchat.EAT_ALL
	
hexchat.hook_command('sudo', sudo, help='/sudo Executes a command as op on channels you have flag +o on.')
hexchat.hook_command('topicappend', topicappend, help='/topicappend Adds a string to the topic')
hexchat.hook_command('appendtopic', topicappend, help='/appendtopic Adds a string to the topic')
hexchat.hook_command('part', disablechan, help='/part parts and disables chan on znc')
hexchat.hook_command('temppart', temppart, help='/temppart parts without disabling chan on znc')
hexchat.hook_command('ignorehost', hostignore, help='/ignorehost ignores a user\'s host')
hexchat.hook_command('unignorehost', hostunignore, help='/unignorehost ignores a user\'s host')
hexchat.hook_command('quiet', quiet, help='/quiet quiets a user')
hexchat.hook_command('unquiet', unquiet, help='/unquiet unquiets a user')
hexchat.hook_command('iexempt', inviteexempt, help='/exempt adds an invite exemption for a user')
hexchat.hook_command('uniexempt', uninviteexempt, help='/unexempt removes an invite exemption for a user')
hexchat.hook_command('exempt', exempt, help='/exempt adds a ban exemption for a user')
hexchat.hook_command('unexempt', unexempt, help='/unexempt removes a ban exemption for a user')
hexchat.hook_command('flags', editflags, help='/flags edits chanserv flags for a user')
hexchat.hook_command('clearstatus', clearstatus, help='/clearstatus closes all ZNC status windows. You can set your prefix at the top of the python file')
hexchat.hook_command('showver', showver)

hexchat.emit_print('Notice', __module_name__ + ' [S]', '%s by %s loaded. You are using version %s of the script.' % (__module_name__, __author__, __module_version__))