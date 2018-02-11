# gpmdpnp.py by ApolloJustice
# for use with Python 3
# non PEP-8 compliant because honestly fuck that
# probably not commented because too lazy

__module_name__ = 'GPMDP NP'
__author__ = 'ApolloJustice'
__module_version__ = '1.0'
__module_description__ = 'Now Playing script for Samuel Attard\'s Google Play Music Desktop Player'

import hexchat, json, sys, os

npskel = "np:\00306 {0} \017by\00307 {1}\017 from\00310 {2}\017 [\00303{3}\017/\00304{4}\017] [\00307GPMDP\017]"
nosongfallback = "np: \00304Playback stopped.\017"

if sys.platform.startswith("linux"): jsonpath = "~/.config/Google Play Music Desktop Player/json_store/playback.json"
elif sys.platform.startswith("darwin"): jsonpath = "~/Library/Application Support/Google Play Music Desktop Player/json_store/playback.json"
elif sys.platform.startswith("win"): jsonpath = "{0}\\Google Play Music Desktop Player\\json_store\\playback.json".format(os.getenv('appdata'))

def prettyprint(status, message):
    hexchat.emit_print('Notice', __module_name__ + ' [{0}]'.format(status), message)

def convertMillis(millis):
    seconds=(millis//1000)%60
    minutes=(millis//(1000*60))%60
    hours=(millis//(1000*60*60))%24
    timestr = ""
    if hours != 0: timestr = timestr + "{}:".format(str(hours))
    timestr = timestr + "{}:".format(str(minutes).zfill(2))
    timestr = timestr + str(seconds).zfill(2)
    return timestr

def getString():
    try:
        with open(jsonpath, encoding="utf8") as data_file:
            data = json.load(data_file)
        if data["playing"] == False: prettyprint("E", "No song playing.")
        title = data["song"]["title"]
        artist = data["song"]["artist"]
        album = data["song"]["album"]
        elapsed = convertMillis(data["time"]["current"])
        duration = convertMillis(data["time"]["total"])
        messagestr = npskel.format(title, artist, album, elapsed, duration)
        return messagestr
    except:
        prettyprint("E", sys.exc_info[0])

def nowplaying(word, word_eol, userdata):
    hexchat.command("me {0}".format(getString()))
    return hexchat.EAT_ALL

hexchat.hook_command("np", nowplaying)
hexchat.emit_print("Notice", __module_name__ + " [S]", "%s by %s loaded. You are using version %s of the script." % (__module_name__, __author__, __module_version__))
