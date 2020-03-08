# chanmsg.py
# this file is part of HexChat-pyscripts
#
# messages multiple channels at once
#
# written by and copyright © 2020 Erica Garcia [ericathesnark] <me@athenas.space>
# licensed under the MIT license [https://license.athenas.space/mit] | SPDX-License-Identifier: MIT
#
# this code says: trans rights
#
# don't like that? suck it up, or write your own code ^-^

__module_name__ = "ChanMsg"
__module_version__ = "1.0"
__module_description__ = "Messages an array of channels"
__author__ = "Erica Garcia [ericathesnark] <me@athenas.space>"

import hexchat


def chanmsg(word, word_eol, userdata):
    chanstr = word[1].split(",")
    for chan in chanstr:
        hexchat.find_context(channel=chan).command("say " + word_eol[2])
    return hexchat.EAT_ALL


hexchat.hook_command("chanmsg", chanmsg)
hexchat.emit_print("Notice", __module_name__ + " [Plugin]", "%s by %s loaded. You are using version %s of the script." % (
    __module_name__, __author__, __module_version__))
