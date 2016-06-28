__module_name__ = 'mpdnp'
__author__ = 'ApolloJustice'
__module_version__ = '1.0'
__module_description__ = 'Now Playing script for Music Player Daemon'

import hexchat
import time

try:
	from mpd import MPDClient
except:
	print('The python-mpd2 module is not installed. unloading.')
	hexchat.command("py unload %s" % __module_name__)


def formattedprint(text):
	hexchat.emit_print("Notice", "%s [S]" % __module_name__,  "%s" % text)

if hexchat.get_pluginpref('ajmpdnp_server') == None:
	formattedprint('Running for the first time. Setting server to \'localhost\'. to change it, /mpdserver <new host>')
	hexchat.set_pluginpref('ajmpdnp_server', 'localhost')
	
if hexchat.get_pluginpref('ajmpdnp_port') == None:
	formattedprint('Running for the first time. Setting port to 6600. to change it, /mpdport <new port>')
	hexchat.set_pluginpref('ajmpdnp_port', '6600')

if hexchat.get_pluginpref('ajmpdnp_pass') == None:
	formattedprint('Running for the first time. Setting password protection to disabled. to enable it, /mpdpass <password>')
	hexchat.set_pluginpref('ajmpdnp_pass', '+-+nopassword+-+')

def np(word, word_eol, userdata):
	server = hexchat.get_pluginpref('ajmpdnp_server')
	port = hexchat.get_pluginpref('ajmpdnp_port')
	password = hexchat.get_pluginpref('ajmpdnp_pass')
	client = MPDClient()
	client.timeout = None
	try:
		client.connect(server, port)
		if password != '+-+nopassword+-+':
			client.password(password)
	except:
		formattedprint("Could not connect to mpd. unloading.")
		hexchat.command('py unload %s' % __module_name__)

	np = client.currentsong()
	st = client.status()
	title = np.get('title')
	artist = np.get('artist')
	album = np.get('album')
	try:
		elapsed = time.strftime("%M:%S", time.gmtime(int(st.get('time').split(':')[0])))
		duration = time.strftime("%M:%S", time.gmtime(int(st.get('time').split(':')[1])))
	except:
		pass
#	playlistpos = st.get('playlist')
#	playlistlength = st.get('playlistlength')
	bitrate = st.get('bitrate')
	playbackstatus = st.get('state')
#	volume = st.get('volume')
#	date = np.get('date')
#	track = np.get('track')
	if playbackstatus == 'pause':
		if not album: 
			hexchat.command('me np:\00306 %s \017by\00307 %s \017 [\00306%s\017/\00310%s\017] [\00302%s\00313kbps\017] [\00304paused\017] [\00325mpd %s\017]' % (title, artist, elapsed, duration, bitrate, client.mpd_version))
		if album: 
			hexchat.command('me np:\00306 %s \017by\00307 %s\017 from\00310 %s\017 [\00306%s\017/\00310%s\017] [\00302%s\00313kbps\017] [\00304paused\017] [\00325mpd %s\017]' % (title, artist, album, elapsed, duration, bitrate, client.mpd_version))
	elif playbackstatus == 'play':
		if not album: 
			hexchat.command('me np:\00306 %s \017by\00307 %s \017 [\00306%s\017/\00310%s\017] [\00302%s\00313kbps\017] [\00325mpd %s\017]' % (title, artist, elapsed, duration, bitrate, client.mpd_version))
		if album: 
			hexchat.command('me np:\00306 %s \017by\00307 %s\017 from\00310 %s\017 [\00306%s\017/\00310%s\017] [\00302%s\00313kbps\017] [\00325mpd %s\017]' % (title, artist, album, elapsed, duration, bitrate, client.mpd_version))
	elif playbackstatus == 'stop':
		hexchat.command('me np: [\00304playback stopped\017] [\00325mpd %s\017]' % client.mpd_version)
	return hexchat.EAT_ALL

def passchange(word, word_eol, userdata):
	if len(word) == 1:
		if hexchat.get_pluginpref('ajmpdnp_pass') == '+-+nopassword+-+':
			formattedprint('Password protection is disabled.')
		else:
			formattedprint('Current mpd password is \'%s\'. To disable password protection, type /mpdpass disable' % hexchat.get_pluginpref('ajmpdnp_pass'))

	if len(word) == 2:
		if word[1].lower() == 'disable':
			formattedprint('Password protection disabled.')
			hexchat.set_pluginpref('ajmpdnp_pass', '+-+nopassword+-+')
		else:
			formattedprint('Password changed to \'%s\'. To disable password protection, type /mpdpass disable' % word[1])
			hexchat.set_pluginpref('ajmpdnp_pass', word[1])

def serverchange(word, word_eol, userdata):
	if len(word) == 1:
		formattedprint('Current mpd hostname is \'%s\'.' % hexchat.get_pluginpref('ajmpdnp_server'))

	if len(word) == 2:
		formattedprint('mpd host changed to \'%s\'.' % word[1])
		hexchat.set_pluginpref('ajmpdnp_server', word[1])

def portchange(word, word_eol, userdata):
	if len(word) == 1:
		formattedprint('Current mpd port is %s.' % hexchat.get_pluginpref('ajmpdnp_port'))

	if len(word) == 2:
		formattedprint('mpd port changed to %s.' % word[1])
		hexchat.set_pluginpref('ajmpdnp_port', word[1])

hexchat.hook_command('np', np)
hexchat.hook_command('mpdpass', passchange)
hexchat.hook_command('mpdport', portchange)
hexchat.hook_command('mpdserver', serverchange)
hexchat.emit_print("Notice", __module_name__ + " [S]", "%s by %s loaded. You are using version %s of the script." % (__module_name__, __author__, __module_version__))