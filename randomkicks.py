# randomkicks.py
# this file is part of hexchat-pyscripts
#
# chooses a kick message randomly from a file
#
# written by and copyright (C) Erica Garcia [athenaorerica] <me@athenas.space> 2019
# licensed under the MIT license [https://mit.athenas.space]
#
# this code says: trans rights
#
# don't like the previous statement? suck it up, or write your own code. ^-^

__module_name__ = "RandomKicks"
__module_version__ = "1.0"
__module_description__ = "Adds a random message to kicks from a file."
__author__ = "Erica Garcia [athenaorerica] <me@athenas.space>"

import hexchat as hexchat
import random

textfiledir = hexchat.get_info("configdir")


def getHost(uList, target):
    for user in uList:
        if user.nick.lower() == target.lower():
            break

    return user


def kickquote(word, word_eol, userdata):
    if len(word) <= 1:
        hexchat.emit_print("Notice", __module_name__, "No arguments given.")
        return hexchat.EAT_ALL

    nick = hexchat.get_info("nick")
    chan = hexchat.get_info("channel")
    userlist = hexchat.get_list("users")
    user = getHost(userlist, word[1])
    host = user.host.split('@')[1]
    isBan = userdata
    line = "No reason specified."

    try:
        line = random.choice(
            open(textfiledir + "\quotes.txt", "r").readlines())
    except:
        hexchat.emit_print("Notice", __module_name__ +
                           " [S]", "Failed to grab a line from quotes.txt (Make sure it's in your config folder!), Using default reason if reason was not specified.")

    if user.nick.lower() == word[1].lower() and isBan is not "":
        hexchat.command("raw mode " + chan + " +b *!*@" + host)

    try:
        reason = word_eol[2]
    except:
        reason = line

    reason = reason.replace('\n', '').replace('\r', '').replace(
        '%k', word[1]).replace('%c', chan).replace('%u', nick)
    hexchat.command("raw kick  " + chan + " " +
                    word[1] + " " + ":" + reason + "%s" % (isBan))

    return hexchat.EAT_ALL


hexchat.hook_command("kick", kickquote, userdata="",
                     help="/kick Kicks a user.")
hexchat.hook_command("kickban", kickquote,
                     userdata=" [Banned]", help="/kickban Kicks and bans a user.")
hexchat.emit_print("Notice", __module_name__ + " [S]", "%s by %s loaded. You are using version %s of the script." % (
    __module_name__, __author__, __module_version__))
