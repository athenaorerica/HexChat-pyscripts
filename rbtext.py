# rbtext.py
# this file is part of hexchat-pyscripts
#
# makes text into a rainbow!
#
# written by and copyright (C) Erica Garcia [athenaorerica] <me@athenas.space> 2019
# licensed under the MIT license [https://mit.athenas.space]
#
# this code says: taste the rainbow, feel the rainbow
#
# don't like the previous statement? suck it up, or write your own code. ^-^

__module_name__ = "RainbowFonts"
__module_version__ = "1.0"
__module_description__ = "Rainbowifies text"
__author__ = "Erica Garcia [athenaorerica] <me@athenas.space>"

import hexchat
import random


def rainbow(word, word_eol, userdata):

    rainbowstr = ""

    for character in word_eol[1]:
        rainbowstr += '\003' + str(random.randint(2, 15)) + character

    hexchat.command("say " + rainbowstr)
    rainbowstr = ""
    return hexchat.EAT_ALL


hexchat.hook_command("rb", rainbow, help="/rb rainbowifies text")
hexchat.emit_print("Notice", __module_name__ + " [S]", "%s by %s loaded. You are using version %s of the script." % (
    __module_name__, __author__, __module_version__))
