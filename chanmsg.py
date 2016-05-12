# chanmsg.py by ApolloJustice
# for use with Python 3
# non PEP-8 compliant because honestly fuck that
# probably not commented because too lazy

# The MIT License
# 
# Copyright (c) 2016 ApolloJustice
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

__module_name__ = "ChanMsg"
__module_version__ = "0.0.1a"
__module_description__ = "Messages an array of channels"
__author__ = "ApolloJustice"

import hexchat

def chanmsg(word, word_eol, userdata):
	chanstr = word[1].split(",")
	for chan in chanstr: hexchat.find_context(channel=chan).command("say " + word_eol[2])
	return hexchat.EAT_ALL
	
hexchat.hook_command("chanmsg", chanmsg)
hexchat.emit_print("Notice", __module_name__ + " [Plugin]", "%s by %s loaded. You are using version %s of the script." % (__module_name__, __author__, __module_version__))