# mentions.py
# this file is part of HexChat-pyscripts
#
# highlight logger for hexchat
#
# written by and copyright © 2020 Erica Garcia [ericathesnark] <me@athenas.space>
# licensed under the MIT license [https://license.athenas.space/mit] | SPDX-License-Identifier: MIT
#
# this code says: trans rights
#
# don't like that? suck it up, or write your own code ^-^

__module_name__ = 'Highlight Logger'
__module_version__ = '1.0'
__module_description__ = 'Prints highlights to another tab'
__author__ = "Erica Garcia [ericathesnark] <me@athenas.space>"

import hexchat
import re


def find_highlighttab(arg1):
    context = hexchat.find_context(channel=arg1)
    if context == None:
        newtofront = hexchat.get_prefs('gui_tab_newtofront')

        hexchat.command('set -quiet gui_tab_newtofront 0')
        hexchat.command('newserver -noconnect {0}'.format(arg1))
        hexchat.command('set -quiet gui_tab_newtofront {}'.format(newtofront))

        return hexchat.find_context(channel=arg1)
    else:
        return context


def highlight_callback(word, word_eol, user_data):

    word = [(word[i] if len(word) > i else '') for i in range(4)]

    highlight_context = find_highlighttab('hilight')
    nick = hexchat.get_info("nick")
    chan = hexchat.get_info('channel')
    net = hexchat.get_info("network")
    sendernick = word[0]
    content = word[1]
    mode = word[2]
    idtext = word[3]

    if 'RasPi ZNC' in net:
        net = net.replace('RasPi ZNC', '').replace('(', '').replace(')', '')
        net = net.lstrip()

    content = re.sub(nick, '\002\00320%s\017' %
                     nick, content, flags=re.IGNORECASE)
    content = content.lstrip()

    if user_data == 'Channel Msg Hilight':
        highlight_context.prnt('{0}[\00327{3}\017] [\00323{4}\017] \00326{1}\00322{2}\017 said: \'{5}\''.format(
            idtext, mode, sendernick, chan, net, content))
    elif user_data == 'Channel Action Hilight':
        highlight_context.prnt(('{0}[\00327{3}\017] [\00323{4}\017] \00326{1}\00322{2}\017 {5}').format(
            idtext, mode, sendernick, chan, net, content))

    highlight_context.command('gui color 3')
    return hexchat.EAT_NONE


hexchat.hook_print('Channel Msg Hilight',
                   highlight_callback, 'Channel Msg Hilight')
hexchat.hook_print('Channel Action Hilight',
                   highlight_callback, 'Channel Action Hilight')
hexchat.emit_print("Notice", __module_name__ + " [S]", "%s by %s loaded. You are using version %s of the script." % (
    __module_name__, __author__, __module_version__))
