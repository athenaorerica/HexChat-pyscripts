# rbtext.py by ApolloJustice
# for use with Python 3
# non PEP-8 compliant because honestly fuck that
# probably not commented because too lazy

__module_name__ = "RainbowFonts"
__module_version__ = "0.1b"
__module_description__ = "Rainbowifies text"
__author__ = "ApolloJustice"

import hexchat
import random

def rainbow(word, word_eol, userdata):

	rainbowstr = ""

	for character in word_eol[1]: rainbowstr += '\003' + str(random.randint(2, 15)) + character

	hexchat.command("say " + rainbowstr)
	rainbowstr = ""
	return hexchat.EAT_ALL

hexchat.hook_command("rb", rainbow, help="/rb rainbowifies text")
hexchat.emit_print("Notice", __module_name__ + " [S]", "%s by %s loaded. You are using version %s of the script." % (__module_name__, __author__, __module_version__))