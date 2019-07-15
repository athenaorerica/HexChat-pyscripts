# autounban.py
# this file is part of HexChat-pyscripts
#
# automatically unbans you using chanserv
#
# written by and copyright © 2019 Erica Garcia [athenaorerica] <me@athenas.space>
# licensed under the MIT license [https://license.athenas.space/mit] | SPDX-License-Identifier: MIT
#
# this code says: trans rights
#
# don't like that? suck it up, or write your own code ^-^

__module_name__ = "AutoUnban"
__module_version__ = "1.0"
__module_description__ = "Unbans you if you have flag +r on a channel"
__author__ = "Erica Garcia [athenaorerica] <me@athenas.space>"

import hexchat

chan = ""
locked = 0

if hexchat.get_pluginpref('aub_alertsenabled') == None:
    hexchat.set_pluginpref('aub_alertsenabled', '1')

if hexchat.get_pluginpref('aub_cooldown') == None:
    hexchat.set_pluginpref('aub_cooldown', '5')


def unban():
    global locked
    if locked == 0:
        hexchat.command('RAW PRIVMSG ChanServ :unban ' + chan)
        hexchat.command('timer 1.5 RAW JOIN ' + chan)
        if hexchat.get_pluginpref("aub_alertsenabled") == 1:
            hexchat.emit_print("Notice", "AutoUB [PL]", "Unbanning yourself from %s. Won't auto-unban for the next %s seconds. [To turn these alerts off, /noaubalerts]" % (
                chan, str(hexchat.get_pluginpref('aub_cooldown'))))
        locked = 1
        cooldown = hexchat.get_pluginpref('aub_cooldown') + 1.5
        hexchat.command('timer %s unlockautounban' % str(cooldown))
        return hexchat.EAT_ALL


def unlock(word, word_eol, userdata):
    global chan
    global locked
    chan = ""
    locked = 0
    if hexchat.get_pluginpref('aub_alertsenabled') == 1:
        hexchat.emit_print(
            "Notice", "AutoUB [PL]", "You will be automatically unbanned from channels again. [To turn these alerts off, /noaubalerts]")
    return hexchat.EAT_ALL


def storechan(word, word_eol, userdata):
    global chan
    chan = word[3]
    unban()


def togglealerts(word, word_eol, userdata):
    setting = hexchat.get_pluginpref('aub_alertsenabled')
    if setting:
        hexchat.emit_print(
            "Notice", "AutoUB [PL]", "You have disabled alerts. To turn them on, /aubtogglealerts")
    else:
        hexchat.emit_print(
            "Notice", "AutoUB [PL]", "You have enabled alerts. To turn them off, /aubtogglealerts")
    hexchat.set_pluginpref('aub_alertsenabled', str(1 - setting))
    return hexchat.EAT_ALL


def chgcooldown(word, word_eol, userdata):
    if len(word) == 1:
        hexchat.emit_print("Notice", "AutoUB [PL]", "Current cooldown is %s seconds." % str(
            hexchat.get_pluginpref('aub_cooldown')))
        return hexchat.EAT_ALL

    hexchat.set_pluginpref('aub_cooldown', word[1])
    hexchat.emit_print("Notice", "AutoUB [PL]", "Cooldown set to %s seconds." % str(
        hexchat.get_pluginpref('aub_cooldown')))


hexchat.hook_server("474", storechan)
hexchat.hook_command("unlockautounban", unlock)
hexchat.hook_command("aubtogglealerts", togglealerts)
hexchat.hook_command("aubcooldown", chgcooldown)
hexchat.emit_print("Notice", __module_name__ + " [S]", "%s by %s loaded. You are using version %s of the script." % (
    __module_name__, __author__, __module_version__))
