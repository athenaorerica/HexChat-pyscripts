# foobar.py
# this file is part of hexchat-pyscripts
#
# wraps easywinampcontrol for use with fb2k
#
# written by and copyright (C) Erica Garcia [athenaorerica] <me@athenas.space> 2019
# licensed under the MIT license [https://mit.athenas.space]
#
# this code says: trans rights
#
# don't like the previous statement? suck it up, or write your own code. ^-^

__module_name__ = "EWC Wrapper"
__module_version__ = "0.0.1a"
__module_description__ = "Wraps easywinampcontrol for use with fb2k"
__author__ = "Erica Garcia [athenaorerica] <me@athenas.space>"

import hexchat


def wrap(word, word_eol, userdata):
    fullstr = word_eol[1].split('|')

    title = fullstr[0]
    artist = fullstr[1]
    album = fullstr[2]
    codec = fullstr[3]
    fb2kver = fullstr[4]
    samplerate = fullstr[5]
    bitrate = fullstr[6]
    soundchannels = fullstr[7]
    elapsed = fullstr[8]
    duration = fullstr[9]

    if duration == "0:0-1":
        hexchat.command("me np: \00304Playback stopped.\017 [\00325fb2k %s\017]" % fb2kver.replace(
            "foobar2000", '').replace('v', '').lstrip().rstrip())
        return hexchat.EAT_ALL

    hexchat.command("me np:\00306 %s \017by\00307 %s\017 from\00310 %s\017 [\00303%s\017/\00304%s\017] [\00318%s\017|\00322%s\00329kbps\017] [\00325fb2k %s\017]" % (
        title, artist, album, elapsed, duration, codec, bitrate, fb2kver.replace("foobar2000", '').replace('v', '').replace(" beta ", 'b').replace(' alpha ', 'a').lstrip().rstrip()))
    return hexchat.EAT_ALL


hexchat.hook_command("reformatwp", wrap)
hexchat.emit_print("Notice", __module_name__ + " [S]", "%s by %s loaded. You are using version %s of the script." % (
    __module_name__, __author__, __module_version__))
