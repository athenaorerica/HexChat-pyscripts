# lastfm.py
# this file is part of HexChat-pyscripts
#
# last.fm now playing script
#
# written by and copyright © 2019 Erica Garcia [athenaorerica] <me@athenas.space>
# licensed under the MIT license [https://license.athenas.space/mit] | SPDX-License-Identifier: MIT
#
# this code says: trans rights
#
# don't like that? suck it up, or write your own code ^-^

__module_name__ = 'lastFM'
__author__ = 'Erica Garcia [athenaorerica] <me@athenas.space>'
__module_version__ = '1.0'
__module_description__ = 'Now Playing script for the LastFM scrobbler'

import hexchat

try:
    import requests
except ImportError:
    hexchat.emit_print(
        "Notice", "LfmNP [PL]", "The Requests python module is not installed. Install it using 'pip install requests' on a terminal or command prompt. Unloading.")
    hexchat.command('py unload %s' % __module_name__)


def announce(word, word_eol, userdata):
    username = hexchat.get_pluginpref('lfm_user')
    apikey = hexchat.get_pluginpref('lfm_key')

    if not username:
        hexchat.emit_print(
            "Notice", "LfmNP [PL]", "No username supplied. /lfmuser [username] to set a username.")
    if not apikey:
        hexchat.emit_print(
            "Notice", "LfmNP [PL]", "No API key supplied. /lfmkey [key] to set an API key.")
    if apikey == None or username == None:
        return hexchat.EAT_ALL

    try:
        r = requests.get(
            r'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=%s&api_key=%s&format=json' % (username, apikey))
    except:
        hexchat.emit_print(
            "Notice", "LfmNP [PL]", "Could not connect to the LastFM servers.")
        return hexchat.EAT_ALL

    jsonReply = r.json()

    try:
        isNP = jsonReply['recenttracks']['track'][0]['@attr']['nowplaying']
    except:
        hexchat.command('me NP: \00304no song playing\017')
        return hexchat.EAT_ALL

    try:
        artist = jsonReply['recenttracks']['track'][0]['artist']['#text']
        title = jsonReply['recenttracks']['track'][0]['name']
        album = jsonReply['recenttracks']['track'][0]['album']['#text']
        if album:
            album = ('\017 from\00310 %s\017' % album)
        hexchat.command("me np:\00306 %s \017by\00307 %s%s \017[\00325LastFM\017]" % (
            title, artist, album))
    except:
        hexchat.emit_print("Notice", "LfmNP [PL]", "Unknown error.")
    return hexchat.EAT_ALL


def changeuser(word, word_eol, userdata):
    username = hexchat.get_pluginpref('lfm_user')

    if not username:
        hexchat.set_pluginpref('lfm_user', word[1])
        hexchat.emit_print(
            "Notice", "LfmNP [PL]", "Set username to '%s'." % word[1])
    if username:
        hexchat.set_pluginpref('lfm_user', word[1])
        hexchat.emit_print(
            "Notice", "LfmNP [PL]", "Set username to '%s'. (was: '%s')" % (word[1], username))


def changekey(word, word_eol, userdata):
    apikey = hexchat.get_pluginpref('lfm_key')

    if not apikey:
        hexchat.set_pluginpref('lfm_key', word[1])
        hexchat.emit_print(
            "Notice", "LfmNP [PL]", "Set apikey to '%s'." % word[1])
    if apikey:
        hexchat.set_pluginpref('lfm_key', word[1])
        hexchat.emit_print(
            "Notice", "LfmNP [PL]", "Set apikey to '%s'. (was: '%s')" % (word[1], apikey))


hexchat.hook_command('lfmuser', changeuser,
                     help='/lfmuser [username] to set a username.')
hexchat.hook_command('lfmkey', changekey,
                     help='/lfmkey [key] to set an API key.')
hexchat.hook_command('np', announce)

hexchat.emit_print("Notice", __module_name__ + " [S]", "%s by %s loaded. You are using version %s of the script." % (
    __module_name__, __author__, __module_version__))
